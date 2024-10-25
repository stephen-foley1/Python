from des import DesKey

# Ask user if they want to encrypt or decrypt
operation = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()

# Ask user for input
key_short = input("Enter a short key: ")
key_short_des = DesKey(bytes(key_short, "utf-8"))

print("Short Key: " + key_short)
print("Short Key Single?: " + str(key_short_des.is_single()))
print("Short Key Triple?: " + str(key_short_des.is_triple()))

key_long = input("Enter a long key: ")
key_long_des = DesKey(bytes(key_long, "utf-8"))

print("Long Key: " + key_long)
print("Long Key Single?: " + str(key_long_des.is_single()))
print("Long Key Triple?: " + str(key_long_des.is_triple()))

key_des = key_short_des

if operation == 'e':
    plaintext = input("Enter plaintext: ")
    plaintext_bytes = bytes(plaintext, "utf-8")
    print("Plaintext: " + plaintext)

    # to use ECB SET ciphertext_bytes = key_des.encrypt(plaintext_bytes, padding=True)
    # to use CBC SET ciphertext_bytes = key_des.encrypt(plaintext_bytes, initial=0, padding=True)
    ciphertext_bytes = key_des.encrypt(plaintext_bytes, initial=0, padding=True)
    ciphertext = ciphertext_bytes.hex()
    print("Ciphertext: " + ciphertext)

elif operation == 'd':
    ciphertext = input("Enter ciphertext (hex): ")
    ciphertext_bytes = bytes.fromhex(ciphertext)
    print("Ciphertext: " + ciphertext)

    # to use ECB SET plaintext_bytes_2 = key_des.decrypt(ciphertext_bytes, padding=True)
    # to use CBC SET plaintext_bytes_2 = key_des.decrypt(ciphertext_bytes, initial=0, padding=True)
    plaintext_bytes_2 = key_des.decrypt(ciphertext_bytes, initial=0, padding=True)
    plaintext_2 = str(plaintext_bytes_2, "utf-8")
    print("Original Plaintext: " + plaintext_2)

else:
    print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")

# output: Original Plaintext: You should avoid DES where possible!