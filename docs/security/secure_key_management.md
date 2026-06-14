# Secure Key Management

## Overview

The Secure OTA Firmware Update Framework relies on asymmetric cryptography for firmware signing and verification.

Private and public keys must be handled securely to preserve trust in the update process.

---

# Private Key

The private key is used to digitally sign firmware packages.

### Security Requirements

- Never store private keys in source code.
- Never commit private keys to GitHub repositories.
- Store keys securely using GitHub Secrets.
- Restrict access to authorized users only.

---

# Public Key

The public key is stored on the IoT edge device.

It is used to verify firmware signatures.

### Security Requirements

- Public keys should remain unchanged.
- Public keys should be protected against unauthorized modification.

---

# Key Rotation

Periodic key rotation improves security.

### Benefits

- Reduces exposure in case of compromise.
- Strengthens trust management.

---

# Access Control

Access to signing keys should follow the principle of least privilege.

Only authorized CI/CD workflows should use the private key.

---

# Conclusion

Proper key management is essential to maintaining firmware authenticity and protecting the OTA infrastructure from unauthorized updates.
