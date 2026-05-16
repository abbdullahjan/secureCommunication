from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import os

def encryptWithAes(message):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = message.encode()
    padded_message = pad(message, AES.block_size)

    ciphertext = cipher.encrypt(padded_message)
    return ciphertext, key, iv

def decryptWithAes(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = cipher.decrypt(ciphertext)
    message = unpad(padded_message, AES.block_size)
    return message.decode()


 