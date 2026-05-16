from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

def encryptWithRSA(data, public_key_str):
    # Import public key
    public_key = RSA.import_key(public_key_str)
    
    # Convert data to number
    message_number = bytes_to_long(data)
    
    # Encrypt: ciphertext = (message ** e) % n
    # pow() is MUCH faster than ** for huge numbers!
    encrypted_number = pow(message_number, public_key.e, public_key.n)
    
    # Convert back to bytes
    encrypted = long_to_bytes(encrypted_number)
    return encrypted

def decryptWithRSA(encrypted_data, private_key_str):
    # Import private key
    private_key = RSA.import_key(private_key_str)
    
    # Convert encrypted data to number
    encrypted_number = bytes_to_long(encrypted_data)
    
    # Decrypt: message = (ciphertext ** d) % n
    # pow() is MUCH faster than ** for huge numbers!
    decrypted_number = pow(encrypted_number, private_key.d, private_key.n)
    
    # Convert back to bytes
    decrypted = long_to_bytes(decrypted_number)
    return decrypted
