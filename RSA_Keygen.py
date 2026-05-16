from Crypto.PublicKey import RSA

def generate_key():    
    # Generate RSA key pair (2048 bits)
    key = RSA.generate(2048)
    
    # Export keys as strings (PEM format)
    private_key_str = key.export_key().decode()
    public_key_str = key.publickey().export_key().decode()
    
    return public_key_str, private_key_str
