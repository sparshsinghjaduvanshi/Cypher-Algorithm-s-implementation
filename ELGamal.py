# ElGamal Implementation

import random

# Modular inverse
def mod_inverse(a, p):
    return pow(a, -1, p)

# Key Generation
def generate_keys(p, g, x):
    y = pow(g, x, p)
    return (p, g, y), x

# Encryption
def encrypt(M, public_key):
    p, g, y = public_key
    k = random.randint(1, p-2)

    C1 = pow(g, k, p)
    C2 = (M * pow(y, k, p)) % p

    return (C1, C2), k

# Decryption
def decrypt(cipher, private_key, p):
    C1, C2 = cipher
    x = private_key

    s = pow(C1, x, p)
    s_inv = mod_inverse(s, p)

    M = (C2 * s_inv) % p
    return M


# -------- Main --------

p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))

public_key, private_key = generate_keys(p, g, x)

print("\nPublic Key:", public_key)
print("Private Key:", private_key)

M = int(input("\nEnter message (number): "))

cipher, k = encrypt(M, public_key)
print("\nRandom k used:", k)
print("Ciphertext (C1, C2):", cipher)

decrypted = decrypt(cipher, private_key, p)
print("Decrypted Message:", decrypted)