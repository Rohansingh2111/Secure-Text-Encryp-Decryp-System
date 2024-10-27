# key_module.py
from cryptography.fernet import Fernet

def generate_key(file_path: str) -> None:
    key = Fernet.generate_key()
    with open(file_path, 'wb') as key_file:
        key_file.write(key)

def load_key(file_path: str) -> bytes:
    try:
        with open(file_path, 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"Key file '{file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error loading key: {str(e)}")
        exit(1)
