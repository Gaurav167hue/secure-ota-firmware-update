
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from logger import log_info, log_error


def verify_signature():

    try:
        # Load public key
        with open("downloads/public_key.pem", "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )

        # Load firmware
        with open("downloads/firmware.bin", "rb") as firmware_file:
            firmware_data = firmware_file.read()

        # Load signature
        with open("downloads/signature.sig", "rb") as signature_file:
            signature = signature_file.read()

        # Verify signature
        public_key.verify(
            signature,
            firmware_data,
            ec.ECDSA(hashes.SHA256())
        )

        log_info("Digital signature verified successfully")
        return True

    except Exception as e:
        log_error(f"Signature verification failed: {e}")
        return False
