
hex_str1 = '1a2b3c4d5e6f'
hex_str2 = '123456789abc'

def xorHexStrings(hex_str1, hex_str2):
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)
    
       # XOR the two integers
    xor_result = int1 ^ int2
    
    # Convert the result back to a hexadecimal string (removing the '0x' prefix)
    return hex(xor_result)[2:]

xor_result = xorHexStrings(hex_str1, hex_str2)

print ("The Xor Result of the two stings is: ", xor_result)

def xor_hex(a, b):
    # XOR two integers after converting from hexadecimal
    return hex(int(a, 16) ^ int(b, 16))[2:]

def verify_xor_properties(a_hex, b_hex, c_hex):
    a = int(a_hex, 16)
    b = int(b_hex, 16)
    c = int(c_hex, 16)

    # Commutative: A ⊕ B = B ⊕ A
    commutative = (a ^ b) == (b ^ a)

    # Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
    associative = (a ^ (b ^ c)) == ((a ^ b) ^ c)

    # Identity: A ⊕ 0 = A
    identity = (a ^ 0) == a

    # Self-Inverse: A ⊕ A = 0
    self_inverse = (a ^ a) == 0

    return commutative, associative, identity, self_inverse

# Sample hexadecimal inputs
a_hex = '1a2b3c4d'
b_hex = '12345678'
c_hex = 'abcdef12'

# Verify properties
commutative, associative, identity, self_inverse = verify_xor_properties(a_hex, b_hex, c_hex)

# Display results
print(f"Commutative: {commutative}")
print(f"Associative: {associative}")
print(f"Identity: {identity}")
print(f"Self-Inverse: {self_inverse}")
