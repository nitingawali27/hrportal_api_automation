import pytest
import datetime
import os

def pytest_configure(config):
    # Define report folder
    reports_dir = r"D:\hrportal_api_automation\reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Create timestamp for report name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(reports_dir, f"report_{timestamp}.html")

    # Set the html report path dynamically
    config.option.htmlpath = report_file
    config.option.self_contained_html = True
