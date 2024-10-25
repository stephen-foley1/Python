import os, time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

before = time.perf_counter()

keyMode = input("Enter key mode user input or random: ").strip().lower()
if keyMode == "user input":
    key = input("Enter Key").strip()
    key_bytes = bytes(key, "utf-8")
    if len(key_bytes) != 32:
        raise ValueError("Invalid key length. Key must be 32 bytes.")
    print("Key: " + key)
elif keyMode == "random":
    key_bytes = os.urandom(32)  # Generating a 32-byte key
    print("Key: " + key_bytes.hex())

nonceType = input("Enter nonce type random or manual: ").strip()
if nonceType == "random":
    nonce_bytes = os.urandom(16)
elif nonceType == "manual":
    nonce = input("Enter nonce: ").strip()
    nonce_bytes = bytes.fromhex(nonce)

chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_encryptor = chacha20_cipher.encryptor()
chacha20_decryptor = chacha20_cipher.decryptor()

mode = input("Encrypt or Decrypt: ").strip().lower()
if mode == "encrypt":
    #plaintext = input("Enter plaintext: ").strip()
    #plaintext_bytes = bytes(plaintext, "utf-8")
    #print("Plaintext: " + plaintext)
    #ciphertext_bytes = chacha20_encryptor.update(plaintext_bytes)
    #ciphertext = ciphertext_bytes.hex()
    #print("Ciphertext: " + ciphertext)

    plaintext_size = int(input("Enter plaintext size in bytes: ").strip())
    plaintext = os.urandom(plaintext_size)  # Generating random plaintext of specified size
    print("Plaintext: " + plaintext.hex())

    ciphertext_bytes = chacha20_encryptor.update(plaintext)
    ciphertext = ciphertext_bytes.hex()
    print("Ciphertext: " + ciphertext)
elif mode == "decrypt":
    ciphertext = input("Enter ciphertext: ").strip()
    ciphertext_bytes = bytes.fromhex(ciphertext)
    print("Ciphertext: " + ciphertext)
    plaintext_bytes_2 = chacha20_decryptor.update(ciphertext_bytes)
    plaintext_2 = str(plaintext_bytes_2, "utf-8")
    print("Original Plaintext: " + plaintext_2)

after = time.perf_counter()
print(f"{after - before:0.4f} seconds")