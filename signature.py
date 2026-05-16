from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import hashlib

def signMessage(message, private_key_str):
    # 1. Hash the message with SHA-256
    hash_obj = hashlib.sha256(message.encode())
    message_hash = hash_obj.digest()  # 32 bytes
    
    # 2. Convert hash to number
    hash_number = bytes_to_long(message_hash)
    
    # 3. Load private key
    private_key = RSA.import_key(private_key_str)
    
    # 4. Sign: signature = hash^d mod n (using private key)
    signature_number = pow(hash_number, private_key.d, private_key.n)
    
    # 5. Convert back to bytes
    signature = long_to_bytes(signature_number)
    
    return signature

def verifySignature(message, signature, public_key_str):
    # 1. Hash the message with SHA-256
    hash_obj = hashlib.sha256(message.encode())
    message_hash = hash_obj.digest()  # 32 bytes
    hash_number = bytes_to_long(message_hash)
    
    # 2. Load public key
    public_key = RSA.import_key(public_key_str)
    
    # 3. Convert signature to number
    signature_number = bytes_to_long(signature)
    
    # 4. Verify: decrypted_hash = signature^e mod n (using public key)
    decrypted_hash_number = pow(signature_number, public_key.e, public_key.n)
    
    # 5. Compare hashes
    if hash_number == decrypted_hash_number:
        return True  
    else:
        return False  

