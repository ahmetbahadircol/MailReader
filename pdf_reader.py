import pdfx
pdf = pdfx.PDFx("30-04-2023.pdf")
text = pdf.reader.text

text_list = text.split("\n")

text_list = [i for i in text_list if not i == ""]