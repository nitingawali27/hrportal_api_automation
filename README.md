# HR Portal API Automation

This repository contains automated test scripts for **HR Portal APIs**, developed using **Python** and **pytest**. It provides end-to-end automated testing, HTML reporting, and is designed for easy maintenance and extension.

The project structure is as follows:

hrportal_api_automation/
│── src/ # Test scripts & logic
│── reports/ # Test reports (HTML)
│── venv/ # Virtual environment
│── configtest.py # Custom pytest configuration
│── requirements.txt # Project dependencies
│── README.md # Project documentation

### Setup and Execution
1. Clone the repository:
```bash
git clone https://github.com/nitingawali27/hrportal_api_automation.git
cd hrportal_api_automation
Create a virtual environment:
python -m venv venv

Activate the virtual environment:
Windows (PowerShell):
.\venv\Scripts\Activate.ps1
Linux/Mac:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt
Run all tests and generate an HTML report:
pytest --html=reports/report.html --self-contained-html

The configtest.py ensures reports are automatically named with date and time, for example:
report_2025-09-14_12-45-30.html
Reports are stored in the reports/ folder, self-contained, and can be opened in any browser.

Tech Stack
Python 3.12+
Pytest
Requests
HTML Reports

Author: Nitin Gawali – Senior QA Engineer
