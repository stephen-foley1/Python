from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

key =input("Enter Key").strip()
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

rc4_cipher = Cipher(algorithms.ARC4(key_bytes), mode=None)
rc4_encryptor = rc4_cipher.encryptor()
rc4_decryptor = rc4_cipher.decryptor()

mode = input("Encrypt or Decrypt: ").strip().lower()
if mode ==  "encrypt":
    plaintext = input("Enter plaintext: ").strip()
    plaintext_bytes = bytes(plaintext, "utf-8")
    print("Plaintext: " + plaintext)

    ciphertext_bytes = rc4_encryptor.update(plaintext_bytes)
    ciphertext = ciphertext_bytes.hex()
    print("Ciphertext: " + ciphertext)


elif mode == "decrypt":
    ciphertext = input("Enter ciphertext: ").strip()
    ciphertext_bytes = bytes.fromhex(ciphertext)
    print("Ciphertext: " + ciphertext)

    plaintext_bytes_2 = rc4_decryptor.update(ciphertext_bytes)
    plaintext_2 = str(plaintext_bytes_2, "utf-8")
    print("Original Plaintext: " + plaintext_2)

else:
    print("Invalid choice")
    exit()

# Output: Ciphertext: eb 3e c6 68 de 7d 9e 02 38 55 44 b9 69 1b c3 8b 9d 56 ab 7d 9d 53 e8 02 c1 86 85 1a d0 5e ad d0 97 2a 75 56 e1 96 2a 60 a1 f6 b2 86 bc 81 11 4a ac bd
# Original Plaintext: You should not use RC4 in real-world applications!
