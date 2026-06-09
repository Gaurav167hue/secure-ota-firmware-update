# Edge Device Verification Logic

## Overview

The Edge Device Verification Agent is responsible for ensuring that only trusted firmware updates are installed on the device.

Before installation, the device performs multiple security checks to verify the authenticity and integrity of the firmware package.

---

## Verification Process

### Step 1: Download Update Package

The device downloads:

- Firmware binary
- Digital signature file
- Manifest file

---

### Step 2: Hash Verification

The device calculates the SHA-256 hash of the downloaded firmware.

The calculated hash is compared with the hash value provided in the manifest.

Result:

- Match → Continue
- Mismatch → Reject update

---

### Step 3: Signature Verification

The device verifies the digital signature using the stored public key.

Result:

- Valid signature → Continue
- Invalid signature → Reject update

---

### Step 4: Version Validation

The device compares the incoming firmware version with the currently installed version.

Result:

- Newer version → Continue
- Older version → Reject update

---

### Step 5: Installation Decision

If all checks pass:

- Install firmware
- Update version information
- Reboot device

If any check fails:

- Stop installation
- Log security event
- Continue running existing firmware

---

## Security Objective

Only firmware that passes integrity, authenticity, and version validation checks is allowed to execute on the device.
