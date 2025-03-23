# Data Entry Web Application

A simple Flask-based web application for collecting and storing data in a CSV file.

## Overview

- **Purpose**: Collect user input through a web form and save it to CSV
- **Tech Stack**: Python, Flask, HTML, CSS
- **Features**:
  - Two text input fields
  - Timestamp recording
  - Automatic CSV creation
  - Responsive design

# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install flask

data-entry-web-app/
├── templates/
│   └── index.html    # Web interface template
├── app.py           # Main application
└── README.md        # Documentation
