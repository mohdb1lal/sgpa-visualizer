from flask import Blueprint, render_template, request, jsonify
from app.pdf_processor import extract_pdf_data

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_files():
    # Initialize dictionaries to store semester data
    semester_data = {sem: {'sgpa': None, 'credits': 0} for sem in range(1, 9)}
    
    for file in request.files.getlist('files'):
        if file.filename.lower().endswith('.pdf'):
            try:
                pdf_data = extract_pdf_data(file.read())
                if pdf_data['semester'] and pdf_data['sgpa']:
                    sem = int(pdf_data['semester'])
                    if 1 <= sem <= 8:
                        semester_data[sem]['sgpa'] = pdf_data['sgpa']
                        semester_data[sem]['credits'] = pdf_data['credits']
            except Exception as e:
                continue
    
    # Calculate CGPA for each semester
    cgpa_values = []
    total_credits_so_far = 0
    total_credit_points_so_far = 0
    
    for i in range(1, 9):
        if semester_data[i]['sgpa'] is not None:
            sem_credits = semester_data[i]['credits']
            sem_sgpa = semester_data[i]['sgpa']
            
            # Add this semester's credit points to the running total
            total_credits_so_far += sem_credits
            total_credit_points_so_far += (sem_sgpa * sem_credits)
            
            # Calculate CGPA up to this semester
            if total_credits_so_far > 0:
                cgpa = total_credit_points_so_far / total_credits_so_far
            else:
                cgpa = None
        else:
            cgpa = None
            
        cgpa_values.append(cgpa)

    return jsonify({
        "semesters": [f"Sem {i}" for i in range(1, 9)],
        "sgpa_values": [semester_data[i]['sgpa'] for i in range(1, 9)],
        "cgpa_values": cgpa_values
    })