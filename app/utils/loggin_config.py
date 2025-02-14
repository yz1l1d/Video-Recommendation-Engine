import logging
import os

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define logging format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),   # Save logs to a file
        logging.StreamHandler()          # Print logs to console
    ]
)

logger = logging.getLogger(__name__)
