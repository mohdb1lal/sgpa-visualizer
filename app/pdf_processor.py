import fitz
import re

def extract_pdf_data(pdf_bytes):
    text = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text().lower()

    # Combined extraction patterns
    semester_match = re.search(
        r'(semester|sem)[\s\-]*s?(\d)',
        text
    )
    
    sgpa_match = re.search(
        r'sgpa[\s:]*(\d+\.\d+)', 
        text
    )

    return {
        'semester': int(semester_match.group(2)) if semester_match else None,
        'sgpa': float(sgpa_match.group(1)) if sgpa_match else None
    }