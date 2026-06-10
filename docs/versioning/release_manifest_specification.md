# Release Manifest Specification

## Overview

The Release Manifest is a metadata file that accompanies each firmware release. It contains essential information required by the IoT Edge Device to validate the authenticity, integrity, and version of the firmware before installation.

The manifest acts as a trusted reference for secure firmware deployment.

---

## Purpose

The Release Manifest provides:

- Firmware identification
- Version information
- Integrity verification data
- Digital signature references
- Build information
- Timestamp information

---

## Manifest Fields

### Firmware Version

Represents the current firmware release version.

Example:

v1.0.0

---

### Build ID

Unique identifier assigned to each firmware build.

Example:

build-2026-001

---

### SHA-256 Hash

Cryptographic hash used to verify firmware integrity.

Example:

3f786850e387550fdab836ed7e6dc881de23001b

---

### Signature File

Reference to the digital signature generated during the signing process.

Example:

firmware.sig

---

### Timestamp

Indicates when the firmware package was created.

Example:

2026-06-10T15:30:00Z

---

### Git Commit ID

Identifies the source code commit associated with the firmware release.

Example:

a1b2c3d4

---

## Example Release Manifest

```json
{
  "firmware_version": "v1.0.0",
  "build_id": "build-2026-001",
  "sha256_hash": "3f786850e387550fdab836ed7e6dc881de23001b",
  "signature_file": "firmware.sig",
  "timestamp": "2026-06-10T15:30:00Z",
  "git_commit_id": "a1b2c3d4"
}
```

---

## Verification Process

The Edge Device downloads the Release Manifest and performs the following checks:

1. Verify SHA-256 hash.
2. Verify digital signature.
3. Validate firmware version.
4. Perform anti-rollback checks.
5. Approve or reject the update.

---

## Security Benefits

The Release Manifest helps provide:

- Firmware authenticity
- Integrity verification
- Traceability
- Version control
- Protection against rollback attacks

---

## Conclusion

The Release Manifest is a critical component of the Secure OTA Firmware Update Framework. It ensures that only authentic and trusted firmware versions are installed on IoT edge devices.
