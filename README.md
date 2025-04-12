# 📊 Academic Progress Tracker - SGPA & CGPA Visualizer

Welcome to the **Academic Progress Tracker**, a sleek and modern tool to visualize your academic journey! This application helps students track their SGPA and CGPA across semesters with an interactive and user-friendly interface.

![Academic Progress Tracker](screenshots/screenshot1.png)

---

## ✨ Features

- **📱 Dark Mode & Light Mode** - Toggle between themes based on your preference
- **📈 SGPA & CGPA Visualization** - Track both metrics in interactive charts
- **🔄 Automatic CGPA Calculation** - Using the formula: `CGPA = (sum(sgpa * credits) / total credits)`
- **💾 Save Progress** - Store your data locally to access it anytime
- **📁 Drag & Drop Upload** - Easily upload your grade cards in PDF format
- **🤖 Smart PDF Analysis** - Automatically extracts semester, SGPA, and credits
- **📊 Export Charts** - Download your progress charts as images
- **📱 Fully Responsive** - Works seamlessly on desktop, tablet, and mobile
- **⚡ Optimized Performance** - Fast loading and smooth animations

---

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js, Font Awesome
- **Backend**: Python, Flask
- **PDF Processing**: PyMuPDF (Fitz)
- **Hosting**: PythonAnywhere

---

## 📂 File Structure

```
academic-progress-tracker/
├── app/                  # Backend logic
│   ├── __init__.py       # Flask app initialization
│   ├── routes.py         # API routes and handlers
│   ├── pdf_processor.py  # Enhanced PDF processing logic
├── static/               # Static files
│   └── styles.css        # Responsive styling with dark mode
├── templates/            # HTML templates
│   └── index.html        # Main interface with improved UX
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

---

## 🚀 How to Run This Application

### **Prerequisites**

- Python 3.8+
- Git (optional)

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/mohdb1lal/sgpa-visualizer.git
cd sgpa-visualizer
```

### **Step 2: Set Up Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Run the Application**

```bash
flask run
```

### **Step 5: Open in Browser**

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Live Demo

Check out the live version of the app here:  
👉 [Click here](http://cplab2022.pythonanywhere.com)

---

## 📱 How to Use

1. **Toggle Dark/Light Mode**: Use the theme toggle in the top-right corner to switch between dark and light themes.
2. **Upload Grade Cards**: Drag and drop your PDF grade cards or click to select files.
3. **View Metrics**: See your current CGPA, latest SGPA, and total completed semesters at a glance.
4. **Explore Charts**: Switch between different chart views using the tabs at the bottom.
5. **Save Your Data**: Click the "Save Data" button to store your academic data locally.
6. **Download Charts**: Click the "Download Chart" button to save your progress chart as an image.

---

## 🤔 FAQ

**Q: What type of PDFs does the application support?**  
A: The app is designed to work with standard university grade cards in PDF format. It can recognize various formats and patterns.

**Q: Is my data private?**  
A: Yes! All processing happens in your browser, and your data is stored locally on your device when you use the "Save Data" feature.

**Q: What if my PDF is not recognized correctly?**  
A: The application uses advanced pattern matching to extract data, but if you encounter issues, please open an issue on GitHub.

**Q: Can I use this for any university?**  
A: The app is designed to be flexible and recognize common grade card formats from various universities.

---

## 🤝 Contributing

We welcome contributions to make this tool even better! Here's how you can help:

1. **Fork the Repository**: Click the "Fork" button on GitHub.
2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Add your awesome code or fixes.
4. **Commit and Push**:
   ```bash
   git commit -m "Add your message here"
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**: Describe your changes and submit!

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Chart.js** for beautiful visualizations
- **PyMuPDF** for PDF processing
- **Font Awesome** for icons
- **All contributors** who help improve this project

---

## 📞 Contact & Support

Have questions, suggestions, or feedback? Feel free to:

- Open an issue on [GitHub](https://github.com/mohdb1lal/sgpa-visualizer/issues)
- Reach out to me at [btechfolks](mailto:btechfolks@gmail.com)

---

## 🚀 Happy Learning!

We hope this tool helps you track your academic progress and achieve your educational goals!
