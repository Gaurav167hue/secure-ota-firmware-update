import json
import hashlib
import os

# Paths
FIRMWARE_PATH = "firmware/firmware.bin"
SIGNATURE_PATH = "Output/signature.sig"
MANIFEST_PATH = "Output/manifest.json"

# Firmware information
VERSION = "1.0.0"
BUILD_ID = "build-001"


def calculate_sha256(file_path):
    """
    Calculate SHA-256 hash of a file.
    """
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


def create_manifest():
    if not os.path.exists(FIRMWARE_PATH):
        print("[ERROR] Firmware file not found.")
        return

    if not os.path.exists(SIGNATURE_PATH):
        print("[ERROR] Signature file not found.")
        return

    firmware_hash = calculate_sha256(FIRMWARE_PATH)

    manifest = {
        "version": VERSION,
        "build_id": BUILD_ID,
        "firmware_file": "firmware.bin",
        "signature_file": "signature.sig",
        "hash_algorithm": "SHA-256",
        "firmware_hash": firmware_hash
    }

    os.makedirs("Output", exist_ok=True)

    with open(MANIFEST_PATH, "w") as manifest_file:
        json.dump(manifest, manifest_file, indent=4)

    print("[SUCCESS] Manifest created successfully.")
    print(f"Saved at: {MANIFEST_PATH}")


if __name__ == "__main__":
    create_manifest()