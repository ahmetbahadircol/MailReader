import imaplib
import os
from text_reader import TextReader

username = TextReader().read("username", "username_and_password.txt")
password = TextReader().read("password", "username_and_password.txt")

server = "outlook.office365.com"

imap = imaplib.IMAP4_SSL(server)

imap.login(username, password)

status, messages = imap.select("INBOX")

print(messages)