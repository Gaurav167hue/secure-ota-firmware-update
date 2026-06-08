# Threat Model

## Attacks Covered

### 1. Man in the Middle Attack

Attacker tries to modify firmware during transfer.
System detects mismatch using digital signature and rejects update.

### 2. Replay Attack

Attacker tries to install old firmware version.
System blocks it using version check.

### 3. Firmware Tampering

Any modification in firmware changes SHA-256 hash.
Verification fails and update is rejected.

## Mitigation Summary

- MITM attack → blocked by digital signature verification
- Replay attack → blocked by version control system
- Firmware tampering → detected using SHA-256 hash mismatch
