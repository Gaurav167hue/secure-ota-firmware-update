# Test Cases

## Overview

This document defines the test cases used to validate the functionality and security of the Secure OTA Firmware Update Framework.

The purpose of these tests is to ensure that firmware updates are securely delivered, verified, and installed while preventing unauthorized or malicious firmware from compromising IoT edge devices.

---

# Test Case TC-001: Valid Firmware Update

## Objective

Verify that a valid firmware package is successfully installed.

## Preconditions

- Firmware package is correctly signed.
- SHA-256 hash matches.
- Incoming version is newer than the installed version.

## Steps

1. Download firmware package.
2. Verify SHA-256 hash.
3. Verify digital signature.
4. Perform version validation.
5. Install firmware.

## Expected Result

- Firmware installation succeeds.
- Device reboots successfully.
- Event is logged.

## Status

Pass

---

# Test Case TC-002: Tampered Firmware Detection

## Objective

Verify that modified firmware is rejected.

## Preconditions

Firmware package contents have been altered.

## Steps

1. Download modified firmware.
2. Calculate SHA-256 hash.
3. Compare with manifest hash.

## Expected Result

- Hash verification fails.
- Firmware installation is rejected.
- Security alert is generated.

## Status

Pass

---

# Test Case TC-003: Invalid Digital Signature

## Objective

Verify that firmware with an invalid signature is rejected.

## Preconditions

Firmware signature does not match the stored public key.

## Steps

1. Download firmware.
2. Perform SHA-256 verification.
3. Verify digital signature.

## Expected Result

- Signature verification fails.
- Firmware update is rejected.
- Event is logged.

## Status

Pass

---

# Test Case TC-004: Rollback Attack Prevention

## Objective

Verify anti-rollback protection.

## Preconditions

Current version:

v1.2.0

Incoming version:

v1.1.0

## Steps

1. Download firmware.
2. Verify hash.
3. Verify signature.
4. Compare versions.

## Expected Result

- Update is rejected.
- Rollback attempt is detected.
- Warning message is generated.

## Status

Pass

---

# Test Case TC-005: Same Version Update

## Objective

Verify that reinstalling the same firmware version is prevented.

## Preconditions

Current version:

v1.2.0

Incoming version:

v1.2.0

## Steps

1. Download firmware.
2. Perform verification.
3. Compare versions.

## Expected Result

- Installation is rejected.
- Duplicate update is prevented.

## Status

Pass

---

# Test Case TC-006: Successful Logging

## Objective

Verify event logging functionality.

## Steps

1. Perform firmware update.
2. Complete installation.

## Expected Result

The system records:

- Firmware version
- Timestamp
- Installation status

## Status

Pass

---

# Test Case TC-007: Corrupted Manifest File

## Objective

Verify handling of invalid manifest metadata.

## Preconditions

Manifest file contains incorrect information.

## Steps

1. Download manifest.
2. Parse metadata.
3. Validate fields.

## Expected Result

- Firmware installation is rejected.
- Error event is logged.

## Status

Pass

---

# Summary

| Test ID | Scenario             | Expected Result  |
| ------- | -------------------- | ---------------- |
| TC-001  | Valid Firmware       | Install Firmware |
| TC-002  | Tampered Firmware    | Reject Update    |
| TC-003  | Invalid Signature    | Reject Update    |
| TC-004  | Rollback Attempt     | Reject Update    |
| TC-005  | Same Version Update  | Reject Update    |
| TC-006  | Logging Verification | Event Logged     |
| TC-007  | Corrupted Manifest   | Reject Update    |

---

## Conclusion

These test cases validate the security, integrity, authenticity, and version control mechanisms implemented in the Secure OTA Firmware Update Framework. Successful execution of these tests demonstrates that the system can securely distribute and install trusted firmware while protecting IoT edge devices from tampering, unauthorized updates, and rollback attacks.
