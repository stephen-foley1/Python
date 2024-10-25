import sys

Key: "mysecretkey"
Plaintext: "myplaintext"

def encrypt_decrypt(input_, key):
    output = bytearray()
    # In Python 3.10 we can use zip(input_, key, strict=True) to
    # ensure that iterables have an equal length
    if len(input_) != len(key):
        raise ValueError("The plaintext and key have different lengths!")
    for (b, c) in zip(input_, key):
        output.append(b ^ c)
    return bytes(output)

if __name__ == "__main__":
    opts = ["-e", "-d"]
    if len(sys.argv) < 2 or sys.argv[1] not in opts:
        print(sys.argv[0] + " [-e|-d]")
        exit(0)

    key_str = input("Key: ")
    key_bytes = bytes(key_str, "utf-8")

    if sys.argv[1] == opts[0]:
        plaintext_str = input("Plaintext: ")
        plaintext_bytes = bytes(plaintext_str, "utf-8")
        ciphertext_bytes = encrypt_decrypt(plaintext_bytes, key_bytes)
        ciphertext_hex = ciphertext_bytes.hex()
        print("Ciphertext (hex): " + ciphertext_hex)
    elif sys.argv[1] == opts[1]:
        ciphertext_hex = input("Ciphertext (hex): ")
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        plaintext_bytes = encrypt_decrypt(ciphertext_bytes, key_bytes)
        plaintext_str = plaintext_bytes.decode("utf-8")
        print("Plaintext: " + plaintext_str)
