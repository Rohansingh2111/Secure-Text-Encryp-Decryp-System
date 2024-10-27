# decryption.py
from cryptography.fernet import Fernet
import base64

def decrypt_text(encrypted_text: str, key: bytes) -> str:
    try:
        fernet = Fernet(key)
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_text.encode('utf-8'))
        decrypted_bytes = fernet.decrypt(encrypted_bytes)
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        return f"Error decrypting text: {str(e)}"
