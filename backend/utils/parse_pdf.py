import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_bytes):
    reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text
