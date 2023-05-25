import email
from text_reader import TextReader
import imaplib
import os
from email.header import decode_header


def login_email_account():
    username = TextReader().read("username", "environment_variables.txt")
    password = TextReader().read("password", "environment_variables.txt")
    server = TextReader().read("server", "environment_variables.txt")

    imap = imaplib.IMAP4_SSL(server)
    imap.login(username, password)

    return imap


def get_email(imap):
    imap.select("INBOX")

    _, selected_mails = imap.search(None, '(FROM "enpara@mailer.enpara.com")')

    _, mail = imap.fetch("3765", "(RFC822)")

    _, bytes_data = mail[0]

    email_message = email.message_from_bytes(bytes_data)

    subject, encoding = decode_header(email_message["Subject"])[0]
    subject = str(subject).split(" ")[0].replace("b'", "").replace(".", "-")

    for part in email_message.walk():
        content_disposition = str(part.get("Content-Disposition"))
        if "attachment" in content_disposition:
            filename = part.get_filename()
            if filename:
                subject += ".pdf"
                print(subject)
                _path_tuple = (os.getcwd(), subject,)
                _full_path = "/".join(_path_tuple)
                open(_full_path, "wb").write(part.get_payload(decode=True))
