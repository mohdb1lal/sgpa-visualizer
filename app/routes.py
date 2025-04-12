from flask import Blueprint, render_template, request, jsonify
import os
from app.pdf_processor import extract_pdf_data
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_files():
    """Process uploaded PDF files and extract academic data."""
    try:
        files = request.files.getlist('files')
        
        if not files or files[0].filename == '':
            return jsonify({
                "error": "No files uploaded"
            }), 400
            
        # Initialize data structure for semester information
        semester_data = {sem: {'sgpa': None, 'credits': 0} for sem in range(1, 9)}
        
        # Process each uploaded file
        for file in files:
            if file and file.filename.lower().endswith('.pdf'):
                try:
                    # Read and analyze PDF data
                    pdf_data = extract_pdf_data(file.read())
                    
                    # If we have valid semester and SGPA data, store it
                    if pdf_data['semester'] and pdf_data['sgpa']:
                        sem = int(pdf_data['semester'])
                        if 1 <= sem <= 8:
                            semester_data[sem]['sgpa'] = pdf_data['sgpa']
                            semester_data[sem]['credits'] = pdf_data['credits'] or 0
                            logger.info(f"Processed semester {sem} with SGPA {pdf_data['sgpa']}")
                except Exception as e:
                    logger.error(f"Error processing file {file.filename}: {str(e)}")
                    continue
        
        # Calculate CGPA for each semester
        cgpa_values = []
        total_credits_so_far = 0
        total_credit_points_so_far = 0
        
        for i in range(1, 9):
            if semester_data[i]['sgpa'] is not None:
                sem_credits = semester_data[i]['credits']
                sem_sgpa = semester_data[i]['sgpa']
                
                # If credits are missing, use a default value of 20
                # This is a fallback in case PDF doesn't contain credit information
                if sem_credits == 0:
                    sem_credits = 20
                    semester_data[i]['credits'] = sem_credits
                
                # Add this semester's credit points to the running total
                total_credits_so_far += sem_credits
                total_credit_points_so_far += (sem_sgpa * sem_credits)
                
                # Calculate CGPA up to this semester
                if total_credits_so_far > 0:
                    cgpa = round(total_credit_points_so_far / total_credits_so_far, 2)
                else:
                    cgpa = None
            else:
                cgpa = None
                
            cgpa_values.append(cgpa)
        
        # Filter out semesters that don't have data
        filled_semesters = []
        filled_sgpa = []
        filled_cgpa = []
        
        for i in range(1, 9):
            if semester_data[i]['sgpa'] is not None:
                filled_semesters.append(f"Sem {i}")
                filled_sgpa.append(semester_data[i]['sgpa'])
                filled_cgpa.append(cgpa_values[i-1])
        
        # Prepare the response data (only including semesters with data)
        response_data = {
            "semesters": filled_semesters,
            "sgpa_values": filled_sgpa,
            "cgpa_values": filled_cgpa
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "error": f"An error occurred while processing files: {str(e)}"
        }), 500