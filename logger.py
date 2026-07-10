import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename="logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Functions
def log_info(message):
    logging.info(message)
    print("[INFO]", message)


def log_warning(message):
    logging.warning(message)
    print("[WARNING]", message)


def log_error(message):
    logging.error(message)
    print("[ERROR]", message)


def log_critical(message):
    logging.critical(message)
    print("[CRITICAL]", message)
