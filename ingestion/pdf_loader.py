from pathlib import Path
from pypdf import PdfReader


def load_pdf(pdf_path):
    """
    Load a PDF document and extract all text.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return {
        "file_name": Path(pdf_path).name,
        "document_type": "PDF",
        "text": text
    }
