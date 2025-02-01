from flask import Blueprint, render_template, request, jsonify
from app.pdf_processor import extract_pdf_data

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_files():
    sgpa_dict = {sem: None for sem in range(1, 9)}
    
    for file in request.files.getlist('files'):
        if file.filename.lower().endswith('.pdf'):
            try:
                pdf_data = extract_pdf_data(file.read())
                if pdf_data['semester'] and pdf_data['sgpa']:
                    sem = int(pdf_data['semester'])
                    if 1 <= sem <= 8:
                        sgpa_dict[sem] = pdf_data['sgpa']
            except Exception as e:
                continue

    return jsonify({
        "semesters": [f"Sem {i}" for i in range(1, 9)],
        "values": [sgpa_dict[i] for i in range(1, 9)]
    })