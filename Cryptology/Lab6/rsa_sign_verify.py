import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024
)

public_key = private_key.public_key()

message = os.urandom(1024)

# We can sign the message using "hash-then-sign".
start = time.perf_counter()
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
end = time.perf_counter()
print(f"Signing Time: {end - start:.4f} seconds")

# We can verify the signature. If the signature is invalid it will
# raise an Exception.
start = time.perf_counter()
public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
end = time.perf_counter()
print(f"Verification Time: {end - start:.4f} seconds")

print()
print("Message: " + message.hex())
print()
print("Signature: " + signature.hex())