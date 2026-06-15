import os
import requests

# Create download directory
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Replace these URLs with your actual GitHub raw URLs
FIRMWARE_URL = "https://github.com/Gaurav167hue/secure-ota-firmware-update/blob/feature/Member1-pki-firmware-signing/firmware/firmware.bin"

SIGNATURE_URL = "https://raw.githubusercontent.com/USERNAME/REPO/BRANCH/Output/signature.sig"

PUBLIC_KEY_URL = "https://github.com/Gaurav167hue/secure-ota-firmware-update/blob/feature/Member1-pki-firmware-signing/keys/public_key.pem"


def download_file(url, filename):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            filepath = os.path.join(DOWNLOAD_DIR, filename)

            with open(filepath, "wb") as file:
                file.write(response.content)

            print(f"[+] {filename} downloaded successfully")

        else:
            print(f"[-] Failed to download {filename}")

    except Exception as e:
        print(f"[ERROR] {e}")


# Download files
download_file(FIRMWARE_URL, "firmware.bin")
download_file(SIGNATURE_URL, "signature.sig")
download_file(PUBLIC_KEY_URL, "public_key.pem")
