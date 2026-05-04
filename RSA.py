# RSA Digital Signature - Full Implementation

import hashlib

# ------------------ Basic Functions ------------------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi

# ------------------ Key Generation ------------------

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # choose e
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# ------------------ Hash Function ------------------

def hash_message(message):
    # Using SHA-256 (realistic for exam)
    hash_obj = hashlib.sha256(message.encode())
    return int(hash_obj.hexdigest(), 16)

# ------------------ Signing ------------------

def sign_message(message, private_key):
    d, n = private_key
    H = hash_message(message)
    signature = pow(H, d, n)
    return signature

# ------------------ Verification ------------------

def verify_signature(message, signature, public_key):
    e, n = public_key
    H1 = hash_message(message)
    H2 = pow(signature, e, n)

    return H1 % n == H2

# ------------------ Main ------------------

# Input primes
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

# Generate keys
public_key, private_key = generate_keys(p, q)

print("\nPublic Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Input message
message = input("\nEnter message: ")

# Sign
signature = sign_message(message, private_key)
print("\nDigital Signature:", signature)

# Verify
if verify_signature(message, signature, public_key):
    print("Signature Verified ")
else:
    print("Invalid Signature ")