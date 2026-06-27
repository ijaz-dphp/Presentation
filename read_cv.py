import docx
import sys

def read_docx(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'Adnan+CV+Updated.docx'
    print(read_docx(filename))
