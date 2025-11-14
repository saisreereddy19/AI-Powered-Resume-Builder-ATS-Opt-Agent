from docx import Document

def extract_text_from_docx(path):
    doc = Document(path)
    text = ""
    for p in doc.paragraphs:
        text += p.text + "\n"
    return text
