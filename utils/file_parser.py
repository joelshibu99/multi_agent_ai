import json
import fitz  # pymupdf for PDF

def detect_format(filepath):
    if filepath.lower().endswith('.pdf'):
        return 'PDF'
    elif filepath.lower().endswith('.json'):
        return 'JSON'
    elif filepath.lower().endswith('.txt') or filepath.lower().endswith('.eml'):
        return 'Email'
    else:
        return 'Unknown'

def extract_content(filepath):
    fmt = detect_format(filepath)
    if fmt == 'PDF':
        return extract_pdf_text(filepath)
    elif fmt == 'JSON':
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif fmt == 'Email':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None

def extract_pdf_text(filepath):
    text = ""
    doc = fitz.open(filepath)
    for page in doc:
        text += page.get_text()
    return text
