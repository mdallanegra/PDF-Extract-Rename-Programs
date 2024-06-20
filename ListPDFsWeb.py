from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
PDF_FOLDER = 'pdfs'  # Folder where PDFs are stored

@app.route('/')
def index():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.lower().endswith('.pdf')]
    return render_template('index.html', pdf_files=pdf_files)

@app.route('/open/<filename>')
def open_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
