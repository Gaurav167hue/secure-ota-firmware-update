# Flowcharts Documentation

## Overview

This document describes the flowcharts used in the Secure OTA Firmware Update and Code Signing Infrastructure project.

These diagrams provide a visual representation of the system architecture, update workflow, verification process, and anti-rollback protection mechanisms.

---

# Flowchart Sequence

The flowcharts are designed to represent the complete lifecycle of firmware development, distribution, verification, and installation.

The sequence of diagrams is as follows:

```text
1. OTA Update Flow
            ↓
2. CI/CD Pipeline Flow
            ↓
3. Firmware Verification Flow
            ↓
4. Anti-Rollback Flow
            ↓
5. Sequence Diagram
```

---

# 1. OTA Update Flow

**Files**

- ota_update_flow.drawio
- ota_update_flow.png

### Purpose

Illustrates the overall firmware update lifecycle from the developer to the IoT edge device.

### Main Components

- IoT Developer
- GitHub Repository
- GitHub Actions CI/CD
- Firmware Signing
- Release Manifest Generation
- OTA Distribution Server
- HTTPS Polling
- Edge Device

---

# 2. CI/CD Pipeline Flow

**Files**

- cicd_pipeline_flow.drawio
- cicd_pipeline_flow.png

### Purpose

Represents the automated build and signing process.

### Main Components

- Developer Push
- GitHub Repository
- GitHub Actions
- Firmware Build
- SHA-256 Hash Generation
- Digital Signature Generation
- Release Manifest Creation
- Upload to OTA Server

---

# 3. Firmware Verification Flow

**Files**

- firmware_verification_flow.drawio
- firmware_verification_flow.png

### Purpose

Shows how the IoT edge device validates firmware before installation.

### Verification Steps

1. Download firmware.
2. Calculate SHA-256 hash.
3. Verify integrity.
4. Verify digital signature.
5. Validate firmware version.
6. Perform anti-rollback checks.
7. Install firmware if all validations succeed.

---

# 4. Anti-Rollback Flow

**Files**

- anti_rollback_flow.drawio
- anti_rollback_flow.png

### Purpose

Prevents installation of outdated firmware versions.

### Main Steps

- Receive firmware.
- Read current version.
- Compare incoming version.
- Reject older firmware.
- Install newer firmware.

---

# 5. Sequence Diagram

**Files**

- sequence_diagram.drawio
- sequence_diagram.png

### Purpose

Represents interactions between system components.

### Component Sequence

```text
Developer
↓
GitHub Repository
↓
GitHub Actions
↓
Firmware Signing Module
↓
OTA Server
↓
IoT Edge Device
↓
Verification Engine
↓
Decision Engine
↓
Install or Reject Update
```

---

# Benefits

These flowcharts provide:

- Better visualization of the OTA update framework.
- Easier understanding of system interactions.
- Improved documentation quality.
- Support for testing and debugging.
- Simplified onboarding for new developers.
- Enhanced maintainability.

---

# Conclusion

The flowcharts collectively describe the complete operation of the Secure OTA Firmware Update Framework, from firmware creation and signing to verification and secure installation on IoT edge devices.
