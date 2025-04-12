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
    
    # Add pattern to extract total credits
    credits_match = re.search(
        r'total credits[\s:]*(\d+(\.\d+)?)',
        text
    )
    
    # If we can't find it with the first pattern, try alternative patterns
    if not credits_match:
        credits_match = re.search(
            r'credits earned[\s:]*(\d+(\.\d+)?)',
            text
        )
    
    # If still not found, try another pattern that might appear in grade cards
    if not credits_match:
        credits_match = re.search(
            r'earned credits[\s:]*(\d+(\.\d+)?)',
            text
        )

    return {
        'semester': int(semester_match.group(2)) if semester_match else None,
        'sgpa': float(sgpa_match.group(1)) if sgpa_match else None,
        'credits': float(credits_match.group(1)) if credits_match else 0
    }