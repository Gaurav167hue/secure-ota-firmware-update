from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate ECDSA Private Key
private_key = ec.generate_private_key(
    ec.SECP256R1()
)

# Convert Private Key Object -> PEM Bytes
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save Private Key
with open("../keys/private_key.pem", "wb") as f:
    f.write(private_bytes)

# Generate Public Key from Private Key
public_key = private_key.public_key()

# Convert Public Key Object -> PEM Bytes
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save Public Key
with open("../keys/public_key.pem", "wb") as f:
    f.write(public_bytes)

print("Private Key saved successfully!")
print("Public Key saved successfully!")

print(private_key)
print(public_key)