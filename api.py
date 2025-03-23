from flask import Flask, render_template, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)

# CSV file path
CSV_FILE = 'records.csv'

def init_csv():
    """Initialize CSV file with headers if it doesn't exist"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'field1', 'field2'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Ensure CSV exists
    init_csv()
    
    # Get form data
    field1 = request.form['field1']
    field2 = request.form['field2']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Append data to CSV
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, field1, field2])
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
