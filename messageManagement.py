import messageEncDec as med
import RSAEncDec
import signature as sig
import binascii
import time

def sendMessage(sender):
    print("\n______________________________\n")
    print("___List of users___")
    print("______________________________\n")
    
    # Read all users
    usersFile = open(r"Files\users.txt", "r")
    Allusers = usersFile.readlines()
    usersFile.close()
    
    # Display all users except sender
    for user in Allusers:
        if user.strip():
            username = user.split(" ")[0]
            if username != sender:
                print(f"- {username}")
    
    print("\n")
    receiver = input("Enter username to send the message: ").lower()
    
    # Check if receiver exists
    receiverExists = False
    for user in Allusers:
        if user.strip():
            username = user.split(" ")[0]
            if username == receiver:
                receiverExists = True
                break
    
    if not receiverExists:
        print("User does not exist! Try again")
        return 0
    
    if receiver == sender:
        print("You cannot send message to yourself!")
        return 0
    
    message = input("Enter your message: ")
    cipherMessage, key, iv = med.encryptWithAes(message)
    
    # now using receivers public key to encrypt aes key
    key = RSAEncDec.encryptWithRSA(key, getPublicKey(receiver))
    
    # sign the message with sender's private key
    message_signature = sig.signMessage(message, getPrivateKey(sender))

    # Convert bytes to hex strings for storage
    cipherHex = binascii.hexlify(cipherMessage).decode()
    keyHex = binascii.hexlify(key).decode()
    ivHex = binascii.hexlify(iv).decode()
    signatureHex = binascii.hexlify(message_signature).decode()
    
    # Save message to file
    messagesFile = open(r"Files\messages.txt", "a")
    messagesFile.write(f"{sender}|{receiver}|{cipherHex}|{keyHex}|{ivHex}|{signatureHex}\n")
    messagesFile.close()
    
    print("Message sent successfully!")
    return 1


def receiveMessage(username):
    print("\n______________________________\n")
    print("         Your Inbox")
    print("______________________________\n")
    
    try:
        messagesFile = open(r"Files\messages.txt", "r")
        allMessages = messagesFile.readlines()
        messagesFile.close()
    except FileNotFoundError:
        print("No messages yet!")
        return
    
    # Filter messages for current user
    userMessages = []
    for msg in allMessages:
        if msg.strip():
            parts = msg.strip().split("|")
            if len(parts) == 6:
                sender, receiver, cipherHex, keyHex, ivHex, signatureHex = parts
                if receiver == username:
                    # Convert hex strings back to bytes
                    cipherMessage = binascii.unhexlify(cipherHex)
                    key = binascii.unhexlify(keyHex)
                    iv = binascii.unhexlify(ivHex)
                    signature = binascii.unhexlify(signatureHex)
                    
                    # decrypting the aes key first
                    key = RSAEncDec.decryptWithRSA(key, getPrivateKey(username))
                    plainText = med.decryptWithAes(cipherMessage, key, iv)
                    
                    # verify signature with sender's public key
                    is_valid = sig.verifySignature(plainText, signature, getPublicKey(sender))
                    
                    userMessages.append((sender, plainText, is_valid))
    
    if len(userMessages) == 0:
        print("No messages for you!")
    else:
        print(f"You have {len(userMessages)} message(s):\n")
        for i, (sender, message, is_valid) in enumerate(userMessages, 1):
            print(f"Message {i}:")
            print(f"From: {sender}")
            print(f"Message: {message}")
            if is_valid:
                print("Signature: Valid")
            else:
                print("Signature: Invalid (Message may be tampered!)")
            print("______________________________\n")
            time.sleep(1)


def getPublicKey(username):
    """Get public key for a username from publicKeyTable.txt"""
    try:
        publicKeyFile = open(r"Files\publicKeyTable.txt", "r")
        allKeys = publicKeyFile.read()
        publicKeyFile.close()
        
        # Find the username in the file
        lines = allKeys.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith(username + " "):
                # Found the username, now collect the key (next lines until END)
                public_key = ""
                for j in range(i, len(lines)):
                    public_key += lines[j].replace(username + " ", "", 1) + "\n"
                    if "-----END PUBLIC KEY-----" in lines[j]:
                        break
                return public_key.strip()
        
        return None  # Username not found
    except FileNotFoundError:
        return None

def getPrivateKey(username):
    """Get private key for a username from PrivateKeys folder"""
    try:
        privateKeyFile = open(f"Files\\PrivateKeys\\{username}.txt", "r")
        private_key = privateKeyFile.read()
        privateKeyFile.close()
        return private_key
    except FileNotFoundError:
        return None
