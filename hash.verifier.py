import hashlib
from logger import log_info, log_error


def calculate_hash(file_path):
    """
    Calculate SHA-256 hash of a file
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        log_error(f"File not found: {file_path}")
        return None


def verify_hash(file_path, expected_hash):
    """
    Compare calculated hash with expected hash
    """

    calculated_hash = calculate_hash(file_path)

    if calculated_hash is None:
        return False

    if calculated_hash == expected_hash:
        log_info("Firmware hash verified successfully")
        return True
    else:
        log_error("Hash verification failed")
        return False
