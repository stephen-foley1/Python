from cryptography.hazmat.primitives.asymmetric import dh

# Step 1: Generate parameters
print("Generating parameters; this can take some time...")
parameters = dh.generate_parameters(generator=2, key_size=512)
parameter_numbers = parameters.parameter_numbers()
p = parameter_numbers.p
g = parameter_numbers.g
print(f"g = {g}")
print(f"p = {p}")

# Step 2: Alice generates her public-private key pair
print("\nGenerating Alice's public-private key pair...")
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()
alice_public_numbers = alice_public_key.public_numbers()
alice_private_numbers = alice_private_key.private_numbers()
A = alice_public_numbers.y
a = alice_private_numbers.x
print(f"Alice's public key (A) = {A}")
print(f"Alice's private key (a) = {a}")

# Save parameters and Alice's keys to a file
with open("alice_keys.txt", "w") as f:
    f.write(f"p = {p}\n")
    f.write(f"g = {g}\n")
    f.write(f"Alice's Public Key = {A}\n")
    f.write(f"Alice's Private Key = {a}\n")

print("\nParameters and Alice's keys have been saved to 'alice_keys.txt'.")

# Read Bob's public key from the file
with open("bob_keys.txt", "r") as f:
    B = int(f.readline().strip().split('=')[1].strip())

# Step 4: Alice computes the shared key using Bob's public key
bob_public_numbers = dh.DHPublicNumbers(B, parameter_numbers)
bob_public_key = bob_public_numbers.public_key()
alice_shared_key_bytes = alice_private_key.exchange(bob_public_key)
print(f"\nShared Key (according to Alice): {alice_shared_key_bytes.hex()}")