from flask import Flask, render_template, send_file
import os
from generate_audit_report import generate_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report')
def generate_report_view():
    generate_report()
    return render_template('report.html')

@app.route('/download_report')
def download_report():
    # Ensure the output directory and file path are correct
    file_path = os.path.join('output', 'final_report.csv')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "Report file not found.", 404

if __name__ == "__main__":
    app.run(debug=True)
