import os
import shutil

# Source files
FIRMWARE_PATH = "firmware/firmware.bin"
SIGNATURE_PATH = "Output/signature.sig"

# Simulated OTA server storage
SERVER_STORAGE = "server_storage"


def upload_to_server(file_path):
    """
    Upload a file to simulated server storage.
    """

    if not os.path.exists(file_path):
        print(f"[ERROR] {file_path} does not exist.")
        return

    os.makedirs(SERVER_STORAGE, exist_ok=True)

    destination = os.path.join(
        SERVER_STORAGE,
        os.path.basename(file_path)
    )

    shutil.copy2(file_path, destination)

    print(f"[SUCCESS] Uploaded {file_path}")
    print(f"Destination: {destination}")
    print("-" * 50)


def main():
    print("\nStarting firmware upload process...\n")

    upload_to_server(FIRMWARE_PATH)
    upload_to_server(SIGNATURE_PATH)

    print("\nFirmware upload completed successfully.")


if __name__ == "__main__":
    main()