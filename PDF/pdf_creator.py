from fpdf import FPDF
import os

pdf = FPDF()

w = 297
h = 210

root_path = r"D:\some\path\to\images"

files = list()

for i in range(10):
    files.append(root_path + str(i) + '.jpg')

for f in files:
    pdf.add_page('L')
    pdf.image(f,0,0, w, h)
    print(f)

pdf.output(r"D:\path\my_document.pdf", "F")

