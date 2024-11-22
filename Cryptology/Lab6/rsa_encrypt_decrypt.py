import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

key_sizes = [1024, 2048, 3072, 7680, 15360]
security_bits = [80, 112, 128, 192, 256]
iterations = 10

def generate_keypair(key_size):
    return rsa.generate_private_key(public_exponent=65537, key_size=key_size)

def measure_keypair_generation_time():
    results = []
    for key_size, security in zip(key_sizes, security_bits):
        times = []
        for _ in range(iterations):
            start = time.perf_counter()
            generate_keypair(key_size)
            end = time.perf_counter()
            times.append(end - start)
        avg_time = sum(times[1:]) / (iterations - 1)  # Ignore the first run
        results.append((security, key_size, avg_time))
    return results

def encrypt_message(public_key, message):
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decrypt_message(private_key, ciphertext):
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def measure_encryption_decryption_time():
    results = []
    long_plaintext = os.urandom(10 * 1024)  # 10KB message
    for key_size, security in zip(key_sizes, security_bits):
        private_key = generate_keypair(key_size)
        public_key = private_key.public_key()

        encryption_times = []
        decryption_times = []
        for _ in range(iterations):
            start = time.perf_counter()
            ciphertext = encrypt_message(public_key, long_plaintext)
            end = time.perf_counter()
            encryption_times.append(end - start)

            start = time.perf_counter()
            decrypt_message(private_key, ciphertext)
            end = time.perf_counter()
            decryption_times.append(end - start)

        avg_enc_time = sum(encryption_times[1:]) / (iterations - 1)  # Ignore the first run
        avg_dec_time = sum(decryption_times[1:]) / (iterations - 1)  # Ignore the first run
        results.append((security, key_size, avg_enc_time, avg_dec_time))
    return results

keypair_generation_times = measure_keypair_generation_time()
print("Keypair Generation Times (in seconds):")
for security, key_size, avg_time in keypair_generation_times:
    print(f"Security: {security}-bits, Key Size: {key_size}-bits, Avg Time: {avg_time:.4f} seconds")

encryption_decryption_times = measure_encryption_decryption_time()
print("Encryption/Decryption Times (in seconds):")
for security, key_size, avg_enc_time, avg_dec_time in encryption_decryption_times:
    print(f"Security: {security}-bits, Key Size: {key_size}-bits, Avg Encryption Time: {avg_enc_time:.4f} seconds, Avg Decryption Time: {avg_dec_time:.4f} seconds")