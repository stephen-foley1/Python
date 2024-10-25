from cryptography.hazmat.primitives.asymmetric import dh

# Read parameters and Alice's public key from the file
with open("alice_parameters.txt", "r") as f:
    p = int(f.readline().strip())
    g = int(f.readline().strip())
    A = int(f.readline().strip())

# Step 1: Construct the parameters from the read values
parameter_numbers = dh.DHParameterNumbers(p, g)
parameters = parameter_numbers.parameters()

# Step 3: Bob generates his public-private key pair
print("\nGenerating Bob's public-private key pair...")
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
bob_public_numbers = bob_public_key.public_numbers()
B = bob_public_numbers.y
print(f"Bob's public key (B) = {B}")

# Save Bob's public key to a file
with open("bob_public_key.txt", "w") as f:
    f.write(f"{B}\n")

print("\nBob's public key has been saved to 'bob_public_key.txt'.")

# Step 5: Bob computes the shared key using Alice's public key
alice_public_numbers = dh.DHPublicNumbers(A, parameter_numbers)
alice_public_key = alice_public_numbers.public_key()
bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
print(f"\nShared Key (according to Bob): {bob_shared_key_bytes.hex()}")