
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os, time


before = time.perf_counter()
keyMode = input("Enter key mode user input or random: ").strip().lower()
if keyMode == "user input":
    key = input("Enter Key").strip()
    key_bytes = bytes(key, "utf-8")
    print("Key: " + key)
elif keyMode == "random":
    keysize = int(input("Enter key size in bytes: ").strip())
    if keysize != 16 and keysize != 24 and keysize != 32:

        if keysize == 16:
            key_bytes= os.urandom(16)
            print("Key: " + key_bytes.hex(), "utf-8")
        elif keysize == 24:
            key_bytes = os.urandom(24)
            print("Key: " + key_bytes.hex(),"utf-8")
        elif keysize == 32:
            key_bytes = os.urandom(32)
            print("Key: " + key_bytes.hex(),"utf-8")
        else:
            raise ValueError("Invalid key length. Key must be 16, 24, or 32 bytes.")

nonceType = input("Enter nonce type random or manual : ").strip()
if nonceType == "random":
    nonce_bytes = os.urandom(16)
elif nonceType == "manual":
    nonce = input("Enter nonce: ").strip()
    nonce_bytes = bytes.fromhex(nonce)

aes_ctr_cipher = Cipher(algorithms.AES(key_bytes),mode=modes.CTR(nonce_bytes))
aes_ctr_encryptor = aes_ctr_cipher.encryptor()
aes_ctr_decryptor = aes_ctr_cipher.decryptor()
mode = input("Encrypt or Decrypt: ").strip().lower()
if mode == "encrypt":
    #plaintext = input("Enter plaintext: ").strip()
    #plaintext_bytes = bytes(plaintext, "utf-8")
    #print("Plaintext: " + plaintext)

    #ciphertext_bytes = aes_ctr_encryptor.update(plaintext_bytes)
    #ciphertext = ciphertext_bytes.hex()
    #print("Ciphertext: " + ciphertext)
    plaintext_size = int(input("Enter plaintext size in bytes: ").strip())
    plaintext = os.urandom(plaintext_size)  # Generating random plaintext of specified size
    print("Plaintext: " + plaintext.hex())

    ciphertext_bytes = aes_ctr_encryptor.update(plaintext)
    ciphertext = ciphertext_bytes.hex()
    print("Ciphertext: " + ciphertext)
elif mode == "decrypt":
    ciphertext = input("Enter ciphertext: ").strip()
    ciphertext_bytes = bytes.fromhex(ciphertext)
    print("Ciphertext: " + ciphertext)
    plaintext_bytes_2 = aes_ctr_decryptor.update(ciphertext_bytes)
    plaintext_2 = str(plaintext_bytes_2, "utf-8")
    print("Original Plaintext: " + plaintext_2)

after = time.perf_counter()
print(f"{after- before:0.4f} seconds")
