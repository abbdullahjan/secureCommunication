# Secure File Management System (SFMS)

A Python-based secure messaging application implementing cryptographic principles for confidential communication.

## Features

- User registration and authentication with SHA-256 password hashing
- RSA-2048 key pair generation for each user
- AES-256 encryption for message confidentiality
- RSA encryption for secure AES key exchange
- Digital signatures using RSA for message integrity verification
- Secure message storage and retrieval

## Security Implementation

**Encryption Flow:**
1. Message encrypted with AES-256 (CBC mode)
2. AES key encrypted with receiver's RSA public key
3. Message signed with sender's RSA private key using SHA-256 hash
4. Signature verified using sender's RSA public key

**Key Management:**
- Public keys stored in `Files/publicKeyTable.txt`
- Private keys stored in `Files/PrivateKeys/{username}.txt`
- User credentials stored with SHA-256 hashed passwords

## Installation

```bash
pip install pycryptodome
```

## Usage

```bash
python Main.py
```

1. Sign up or log in
2. Send encrypted messages to other users
3. View inbox with automatic signature verification

## Project Structure

```
├── Main.py                  # Entry point
├── loginSignup.py          # User authentication
├── RSA_Keygen.py           # RSA key generation
├── RSAEncDec.py            # RSA encryption/decryption
├── messageEncDec.py        # AES encryption/decryption
├── signature.py            # Digital signature functions
├── messageManagement.py    # Message handling
└── Files/
    ├── users.txt           # User credentials
    ├── publicKeyTable.txt  # Public keys
    ├── messages.txt        # Encrypted messages
    └── PrivateKeys/        # Private key storage
```

## Technologies

- Python 3.x
- PyCryptodome (AES, RSA)
- hashlib (SHA-256)

## Note

This is an educational project demonstrating cryptographic concepts. Not intended for production use.
