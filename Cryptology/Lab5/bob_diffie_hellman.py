from cryptography.hazmat.primitives.asymmetric import dh

# Read parameters and Alice's public key from the file
with open("alice_keys.txt", "r") as f:
    p = int(f.readline().strip().split('=')[1].strip())
    g = int(f.readline().strip().split('=')[1].strip())
    A = int(f.readline().strip().split('=')[1].strip())

# Step 1: Construct the parameters from the read values
parameter_numbers = dh.DHParameterNumbers(p, g)
parameters = parameter_numbers.parameters()

# Step 3: Bob generates his public-private key pair
print("\nGenerating Bob's public-private key pair...")
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
bob_public_numbers = bob_public_key.public_numbers()
bob_private_numbers = bob_private_key.private_numbers()
B = bob_public_numbers.y
b = bob_private_numbers.x
print(f"Bob's public key (B) = {B}")
print(f"Bob's private key (b) = {b}")

# Save Bob's keys to a file
with open("bob_keys.txt", "w") as f:
    f.write(f"Bob's Public Key = {B}\n")
    f.write(f"Bob's Private Key = {b}\n")

print("\nBob's keys have been saved to 'bob_keys.txt'.")

# Step 5: Bob computes the shared key using Alice's public key
alice_public_numbers = dh.DHPublicNumbers(A, parameter_numbers)
alice_public_key = alice_public_numbers.public_key()
bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
print(f"\nShared Key (according to Bob): {bob_shared_key_bytes.hex()}")