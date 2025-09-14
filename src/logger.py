import logging
import os
from datetime import datetime

# Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # This creates the folder if it doesn't exist

# Log file with timestamp
log_file = os.path.join(LOG_DIR, f"hrportal_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Create logger
LOGGER = logging.getLogger("HRPortalLogger")
LOGGER.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Console handler (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
LOGGER.addHandler(file_handler)
LOGGER.addHandler(console_handler)

# Test log (optional)
if __name__ == "__main__":
    LOGGER.info("Logger initialized and logs directory created successfully.")
