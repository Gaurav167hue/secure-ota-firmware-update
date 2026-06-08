# Security Rules for OTA System

## 1. Firmware Integrity Rule

Every firmware must pass SHA-256 hash verification before installation.

---

## 2. Signature Verification Rule

Firmware must be digitally signed using private key and verified using public key on the device.

If signature verification fails → firmware is rejected.

---

## 3. Version Control Rule

- Device will only accept newer firmware versions
- Downgrade (rollback) is strictly blocked

---

## 4. Trusted Source Rule

Firmware updates are only accepted from authorized CI/CD pipeline.

Any external or unknown source is rejected.

---

## 5. Failure Handling Rule

If verification fails:

- Installation is stopped immediately
- Event is logged as "SECURITY ALERT"
- Device continues running previous safe firmware
