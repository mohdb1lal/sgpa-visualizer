# 📊 SGPA Visualizer [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/sgpa-visualizer/blob/main/LICENSE)

A modern web application to visualize academic progress from university grade cards. Perfect for students to track their SGPA trends across semesters!

![App Screenshot](screenshot.png)

## 🌟 Features

- 🚀 Drag & drop PDF grade card upload
- 📈 Interactive SGPA progress chart
- 🎨 Modern UI with responsive design
- 🔍 Automatic semester detection
- 📱 Mobile-friendly interface
- 🛠️ Built-in error handling and validation

## 🛠️ Tech Stack

**Frontend:**  
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat&logo=chart.js&logoColor=white)

**Backend:**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-009688?style=flat&logo=adobe-acrobat-reader&logoColor=white)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sgpa-visualizer.git
cd sgpa-visualizer
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

```bash
flask run
```

Open http://localhost:5000 in your browser

## 📂 Project Structure

```
sgpa-visualizer/
├── app/              # Backend application
├── static/           # CSS and assets
├── templates/        # HTML templates
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [Chart.js](https://www.chartjs.org/) for interactive visualizations
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF processing
- College academic department for sample grade cards
