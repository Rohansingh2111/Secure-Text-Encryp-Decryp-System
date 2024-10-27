from encrypt_module import encrypt_text
from decrypt_module import decrypt_text
from key_module import generate_key, load_key
import os

def main():
    print("Secure Text Encryption and Decryption System")
    print("Choose an option:")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Generate a New Key")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        key_path = input("Enter path to key file: ").strip()
        key = load_key(key_path)
        text = input("Enter text to encrypt: ")
        encrypted_text = encrypt_text(text, key)
        print("Encrypted text:", encrypted_text)

    elif choice == '2':
        key_path = input("Enter path to key file: ").strip()
        key = load_key(key_path)
        encrypted_text = input("Enter text to decrypt: ")
        decrypted_text = decrypt_text(encrypted_text, key)
        print("Decrypted text:", decrypted_text)

    elif choice == '3':
        key_path = input("Enter path to save the new key: ").strip()
        generate_key(key_path)
        print("New key generated and saved to:", key_path)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
