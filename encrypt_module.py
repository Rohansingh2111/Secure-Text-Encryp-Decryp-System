# encryption.py
from cryptography.fernet import Fernet
import base64

def encrypt_text(plain_text: str, key: bytes) -> str:
    fernet = Fernet(key)
    encrypted_bytes = fernet.encrypt(plain_text.encode())
    return base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')
