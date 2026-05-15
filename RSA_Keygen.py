from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_key():    
    private_key = rsa.generate_private_key(
        public_exponent=65537,   # standard e value
        key_size=2048            # bits — 2048 is minimum safe today
    )

    public_key = private_key.public_key()

    private_key_str = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
    ).decode("utf-8")

    # Convert public key object to string
    public_key_str = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode("utf-8")
    
    return public_key_str, private_key_str
