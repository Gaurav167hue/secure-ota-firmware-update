# Anti-Rollback Mechanism

## Introduction

The Anti-Rollback Mechanism is a security feature designed to prevent IoT devices from installing older firmware versions. This mechanism protects devices from downgrade attacks, where an attacker attempts to replace the current firmware with a vulnerable previous version.

In a secure OTA (Over-The-Air) update system, firmware versions should always move forward. Allowing older firmware installations may reintroduce security vulnerabilities that were previously fixed.

---

## Purpose

The primary objectives of the Anti-Rollback Mechanism are:

- Prevent firmware downgrade attacks
- Ensure devices always run the latest approved firmware
- Protect against known vulnerabilities in older versions
- Maintain firmware integrity and security
- Improve overall device reliability

---

## What is a Rollback Attack?

A rollback attack occurs when an attacker forces a device to install an older firmware version instead of the latest secure release.

### Example

Current Installed Firmware:

Version: 1.2.0

## Incoming Firmware Version:

Version: 1.0.0

Although Version 1.0.0 may be digitally signed, it may contain vulnerabilities that have already been fixed in Version 1.2.0.

Without rollback protection, the device may accept the outdated firmware and become vulnerable again.

# Anti-Rollback Strategy-

The system maintains a record of the currently installed firmware version.

Before installing a new update, the device compares:

Current Firmware Version
Incoming Firmware Version

The update is only accepted if the incoming version is newer than the installed version.

Version Validation Process
Step 1: Read Current Version

The device retrieves the currently installed firmware version.

# Example:

Current Version = 1.2.0
Step 2: Read Incoming Version

The device reads the version number from the firmware manifest.

# Example:

Incoming Version = 1.3.0
Step 3: Compare Versions

The device compares both version numbers.

Step 4: Make Decision

Based on the comparison result, the firmware is either accepted or rejected.

Decision Matrix

| Current Version | Incoming Version | Result   |
| --------------- | ---------------- | -------- |
| 1.0.0           | 1.1.0            | Accepted |
| 1.0.0           | 1.0.0            | Rejected |
| 1.1.0           | 1.0.0            | Rejected |
| 1.2.0           | 1.3.0            | Accepted |

# Security Rules:

Rule 1: Only Newer Versions Are Allowed

The incoming firmware version must be greater than the currently installed version.

Rule 2: Same Version Is Rejected

Reinstallation of the same firmware version is not allowed.

Rule 3: Older Versions Are Rejected

Any firmware version lower than the current version is automatically rejected.

Rule 4: Verification Before Installation

# The firmware must successfully pass:

SHA-256 Hash Verification
Digital Signature Verification

Only after successful verification should version validation occur.

Integration with OTA Update Process

The Anti-Rollback Mechanism works as part of the complete OTA verification workflow.

# Update Flow:

Download firmware package.

Verify SHA-256 hash.

Verify digital signature.

Check firmware version.

Accept or reject installation.

This ensures that both authenticity and version integrity are maintained.

Security Benefits
Protection Against Downgrade Attacks

Prevents attackers from installing vulnerable firmware versions.

# Improved Device Security

Ensures devices always run the latest secure release.

Version Consistency

Maintains consistent firmware versions across all deployed devices.

Better Auditability

Provides traceable firmware upgrade history.

Reduced Attack Surface

Eliminates risks associated with outdated software.

# Logging Requirements

Whenever a rollback attempt is detected, the system should generate a security log.

# Example:

[SECURITY ALERT]

Rollback attempt detected

Current Version : 1.2.0
Incoming Version: 1.0.0

Action: Update Rejected

These logs help administrators identify suspicious activities and maintain audit records.

# Future Enhancements

Hardware-backed version storage.

TPM-based protection.

Secure Boot integration.

Signed firmware manifests.

Centralized monitoring dashboard.

# Conclusion

The Anti-Rollback Mechanism is a critical component of the Secure OTA Firmware Update Framework. By enforcing strict version validation policies, the system prevents downgrade attacks and ensures that only trusted and up-to-date firmware versions are installed on IoT devices.
