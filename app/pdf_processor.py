import fitz
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_pdf_data(pdf_bytes):
    """
    Extract academic data (semester, SGPA, credits) from PDF grade cards.
    
    Args:
        pdf_bytes: The raw bytes of the PDF file
        
    Returns:
        dict: A dictionary containing extracted data with keys:
            - semester: The semester number (int)
            - sgpa: The SGPA value (float)
            - credits: The total credits for the semester (float)
    """
    text = ""
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text().lower()
    except Exception as e:
        logger.error(f"Error opening PDF: {str(e)}")
        raise ValueError(f"Invalid PDF format: {str(e)}")
    
    # Skip processing if the text is too short (likely not a valid grade card)
    if len(text) < 50:
        logger.warning("PDF content too short, may not be a valid grade card")
        return {
            'semester': None,
            'sgpa': None,
            'credits': 0
        }
    
    # Extract semester with more comprehensive patterns
    semester_patterns = [
        r'(semester|sem)[\s\-]*s?(\d)',  # Basic pattern: semester 3, sem-4, etc.
        r'(semester|sem)[\s:]*(i{1,3}|iv|v|vi|vii|viii)',  # Roman numerals: semester I, semester II
        r'(\d)(st|nd|rd|th)[\s]*(semester|sem)',  # Ordinal patterns: 1st semester, 3rd sem
        r'semester[\s\-]*(\d+)'  # Simple number after "semester"
    ]
    
    semester = None
    for pattern in semester_patterns:
        semester_match = re.search(pattern, text)
        if semester_match:
            # For Roman numerals, convert to integers
            if semester_match.group(2) in ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii']:
                roman_to_int = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8}
                semester = roman_to_int.get(semester_match.group(2).lower())
            else:
                try:
                    semester = int(semester_match.group(2))
                except (IndexError, ValueError):
                    # Might be a pattern where semester number is in group 1
                    try:
                        semester = int(semester_match.group(1))
                    except (IndexError, ValueError):
                        continue
            break
    
    # If we couldn't find semester, try to look for year and convert to semester
    if semester is None:
        year_match = re.search(r'(first|second|third|fourth|1st|2nd|3rd|4th)[\s-]year', text)
        if year_match:
            year_mapping = {
                'first': 1, 'second': 3, 'third': 5, 'fourth': 7,
                '1st': 1, '2nd': 3, '3rd': 5, '4th': 7
            }
            year = year_match.group(1).lower()
            semester = year_mapping.get(year)
    
    # Extract SGPA with more robust patterns
    sgpa_patterns = [
        r'sgpa[\s:]*(\d+\.\d+)',  # Basic: sgpa: 8.5, sgpa 9.1
        r'sgpa[\s\-]*:[\s\-]*(\d+\.\d+)',  # With various separators
        r'sgpa[\s\-]*[=][\s\-]*(\d+\.\d+)',  # With equals sign
        r'sgpa[\s\-]*obtained[\s\-:]*(\d+\.\d+)',  # Descriptive format
        r'semester[\s\-]*(grade|point)[\s\-]*(average|point)[\s\-:=]*(\d+\.\d+)'  # Full SGPA term
    ]
    
    sgpa = None
    for pattern in sgpa_patterns:
        sgpa_match = re.search(pattern, text)
        if sgpa_match:
            try:
                # The SGPA value might be in different capture groups depending on the pattern
                if pattern.count('(') == 3:  # For the last pattern with 3 capture groups
                    sgpa = float(sgpa_match.group(3))
                else:
                    sgpa = float(sgpa_match.group(1))
                break
            except (IndexError, ValueError):
                continue
    
    # Extract credits with various patterns
    credit_patterns = [
        r'total[\s\-]*(credits|credit)[\s:]*(\d+\.?\d*)',
        r'credits[\s\-]*(earned|obtained|completed)[\s:]*(\d+\.?\d*)',
        r'(earned|obtained|completed)[\s\-]*credits[\s:]*(\d+\.?\d*)',
        r'credit[\s\-]*(points|hours)[\s:]*(\d+\.?\d*)',
        r'(\d+\.?\d*)[\s\-]*credits[\s\-]*(earned|obtained|completed)'
    ]
    
    credits = 0
    for pattern in credit_patterns:
        credits_match = re.search(pattern, text)
        if credits_match:
            try:
                credits = float(credits_match.group(2))
                break
            except (IndexError, ValueError):
                try:
                    credits = float(credits_match.group(1))
                except (IndexError, ValueError):
                    continue
    
    # If no credits found, try to count credits from individual subjects
    if credits == 0:
        # Look for patterns like "4 credits" or "credits: 3" throughout the document
        subject_credits = re.findall(r'(\d+)[\s\-]*(credit|cr)', text)
        if subject_credits:
            try:
                credits = sum(int(c[0]) for c in subject_credits)
            except (ValueError, IndexError):
                pass
    
    # Log the extraction results for debugging
    logger.info(f"Extracted data - Semester: {semester}, SGPA: {sgpa}, Credits: {credits}")
    
    # If we couldn't find semester or SGPA, return None values
    if semester is None or sgpa is None:
        logger.warning("Could not extract required information from PDF")
        
    # Default credits to 20 if not found but SGPA is available
    if credits == 0 and sgpa is not None:
        credits = 20
        logger.info(f"Using default credits value of 20")
    
    return {
        'semester': semester,
        'sgpa': sgpa,
        'credits': credits
    }