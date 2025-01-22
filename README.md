# SGPA Analyzer

A web application that analyzes and visualizes semester-wise SGPA progression from KTU (APJ Abdul Kalam Technological University) grade cards. Upload your semester PDFs and get instant visualization of your academic performance.

## 🚀 Features

- **PDF Processing**

  - Upload multiple semester grade cards in PDF format
  - Automatic SGPA extraction
  - Support for KTU grade card format
  - Error handling for invalid/corrupt PDFs

- **Visualization**

  - Interactive line graph showing SGPA progression
  - Semester-wise performance tracking
  - Responsive and dynamic charts using Plotly
  - Export options for graphs

- **Analysis**
  - Calculate overall performance metrics
  - View semester-wise statistics
  - Track performance trends
  - Detailed statistical summary

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Streamlit** - Web interface
- **PyPDF2** - PDF processing
- **Plotly** - Data visualization
- **Pandas** - Data manipulation
- **pytest** - Testing framework

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for version control)

## 💻 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sgpa-analyzer.git
cd sgpa-analyzer
```

2. **Create and activate virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Start the application**

```bash
streamlit run src/app.py
```

2. **Access the web interface**

- Open your browser
- Navigate to `http://localhost:8501`

3. **Upload grade cards**

- Click on "Upload PDFs" button
- Select one or more KTU grade card PDFs
- View the generated visualization and analysis

## 📁 Project Structure

```
sgpa-vizualizer/
├── data/
│   └── grade_cards/    # Store uploaded PDFs here
├── src/
│   ├── __init__.py
│   ├── app.py                 # Main Streamlit application
│   └── utils/
│       ├── __init__.py
│       ├── pdf_processor.py   # PDF processing utilities
│       └── visualizer.py      # Data visualization utilities
├── tests/
│   ├── __init__.py
│   ├── test_pdf_processor.py  # PDF processor tests
│   └── test_visualizer.py     # Visualizer tests
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## 📝 Development Guidelines

1. **Code Style**

   - Follow PEP 8 guidelines
   - Use meaningful variable names
   - Add docstrings for functions and classes

2. **Testing**

   - Write tests for new features
   - Maintain test coverage
   - Run tests before committing

3. **Version Control**
   - Create feature branches
   - Write clear commit messages
   - Keep commits focused and atomic

## 🔍 Future Enhancements

- [ ] Support for different university grade card formats
- [ ] CGPA prediction based on current trends
- [ ] Enhanced statistical analysis
- [ ] Multiple visualization options
- [ ] PDF batch processing
- [ ] Export functionality for reports
- [ ] User authentication system
- [ ] Grade card data backup

## 🐛 Known Issues

- Currently supports only KTU grade card format
- Limited to PDF files only
- Requires specific PDF formatting

## 📫 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/sgpa-analyzer](https://github.com/yourusername/sgpa-analyzer)

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- APJ Abdul Kalam Technological University
- Streamlit Documentation
- PyPDF2 Documentation
- Plotly Community
