import os
from pdf2docx import Converter

for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdf_file = file
        docx_file = file.replace('.pdf', '.docx')
        print(f'Converting {pdf_file} to {docx_file}')
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
