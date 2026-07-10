# secure-ota-firmware-update
Secure OTA Firmware Update and Code Signing Infrastructure
# Edge Device Verification Agent

## Overview

This project simulates an IoT Edge Device responsible for securely validating firmware updates before installation.

The device performs:

* Firmware download
* SHA-256 hash verification
* Digital signature verification
* Security logging
* Firmware installation or rejection

---

## Project Structure

```
edge-device-verification/
│
├── device_agent.py
├── firmware_downloader.py
├── hash_verifier.py
├── signature_verifier.py
├── logger.py
├── downloads/
│   ├── firmware.bin
│   ├── signature.sig
│   └── public_key.pem
└── logs/
    └── security.log
```

---

## Technologies Used

* Python
* requests
* cryptography
* hashlib
* logging

---

## Workflow

1. Download firmware files.
2. Verify SHA-256 hash.
3. Verify digital signature using public key.
4. Install firmware if verification succeeds.
5. Reject update and generate security logs if verification fails.

---

## Security Features

* Firmware integrity validation
* Digital signature verification
* Tampering detection
* Security event logging
* Secure update mechanism

---

## Running the Project

Install dependencies:

```bash
pip install requests cryptography
```

Run:

```bash
python device_agent.py
```

---

## Expected Output

### Success

```
[INFO] Firmware hash verified successfully
[INFO] Digital signature verified successfully
[INFO] Installing firmware...
[INFO] Device rebooted successfully
```

### Failure

```
[ERROR] Hash verification failed
[CRITICAL] Firmware update rejected
[CRITICAL] Security alert generated
```

---

## Author

Member 2 – Edge Verification Agent

Advanced Cybersecurity Internship Project
