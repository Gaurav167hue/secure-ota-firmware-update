from hash_verifier import verify_hash
from signature_verifier import verify_signature
from logger import log_info, log_error, log_critical


def install_firmware():
    log_info("Installing firmware...")
    log_info("Device rebooted successfully")


def reject_update():
    log_critical("Firmware update rejected")
    log_critical("Security alert generated")


def main():

    log_info("Simulated IoT Device Started")

    # Hash verification
    if not verify_hash("downloads/firmware.bin"):
        log_error("Hash verification failed")
        reject_update()
        return

    # Signature verification
    if not verify_signature():
        log_error("Signature verification failed")
        reject_update()
        return

    # Firmware installation
    install_firmware()


if __name__ == "__main__":
    main()
