from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def get_iv():
    iv = input("Enter the IV (hex) or leave blank to generate a random IV: ").strip()
    if iv:
        return bytes.fromhex(iv)
    else:
        return os.urandom(16)

# Ask user if they want to encrypt or decrypt
operation = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()

# Ask user for the mode of operation
mode = input("Choose mode (ECB, CBC, CFB, OFB): ").strip().upper()

# Ensure the key length is valid for AES (16, 24, or 32 bytes)
key = input("Enter the key (16, 24, or 32 bytes): ").strip()
key_bytes = bytes.fromhex(key) if all(c in '0123456789abcdefABCDEF' for c in key) else bytes(key, "utf-8")
if len(key_bytes) not in [16, 24, 32]:
    raise ValueError("Invalid key length. Key must be 16, 24, or 32 bytes.")
print("Key: " + key)

# Initialize the AES Cipher based on the chosen mode
if mode == 'ECB':
    aes_cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
elif mode == 'CBC':
    iv = get_iv()
    print("IV:", iv.hex())
    aes_cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
elif mode == 'CFB':
    iv = get_iv()
    print("IV:", iv.hex())
    aes_cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv), backend=default_backend())
elif mode == 'OFB':
    iv = get_iv()
    print("IV:", iv.hex())
    aes_cipher = Cipher(algorithms.AES(key_bytes), modes.OFB(iv), backend=default_backend())
else:
    raise ValueError("Invalid mode. Choose from ECB, CBC, CFB, OFB.")

if operation == 'e':
    plaintext = input("Enter plaintext: ").strip()
    plaintext_bytes = bytes.fromhex(plaintext) if all(c in '0123456789abcdefABCDEF' for c in plaintext) else bytes(plaintext, "utf-8")
    print("Plaintext: " + plaintext)

    # Encrypting the plaintext (no padding for ECB mode)
    aes_encryptor = aes_cipher.encryptor()  # Create encryptor instance
    ciphertext_bytes = aes_encryptor.update(plaintext_bytes) + aes_encryptor.finalize()
    ciphertext = ciphertext_bytes.hex()
    print("Ciphertext: " + ciphertext)

elif operation == 'd':
    ciphertext = input("Enter ciphertext (hex): ").strip()
    ciphertext_bytes = bytes.fromhex(ciphertext)
    print("Ciphertext: " + ciphertext)

    # Decrypting the ciphertext
    aes_decryptor = aes_cipher.decryptor()  # Create decryptor instance
    decrypted_bytes = aes_decryptor.update(ciphertext_bytes) + aes_decryptor.finalize()

    # No unpadding for ECB mode
    try:
        plaintext_2 = decrypted_bytes.decode("utf-8")
        print("Original Plaintext: " + plaintext_2)
    except UnicodeDecodeError as e:
        print(f"Error decoding plaintext: {e}")
    except ValueError as e:
        print(f"Error during decryption: {e}")

else:
    print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")