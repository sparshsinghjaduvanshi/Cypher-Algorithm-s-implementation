# Diffie-Hellman Key Exchange

def mod_exp(base, exp, mod):
    # Efficient modular exponentiation
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
        
    return result


def diffie_hellman():
    # Public values
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root (g): "))
    
    # Private keys
    a = int(input("Enter private key for Alice: "))
    b = int(input("Enter private key for Bob: "))
    
    # Public keys
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    
    print("\nPublic key of Alice:", A)
    print("Public key of Bob:", B)
    
    # Shared secret keys
    key_A = mod_exp(B, a, p)
    key_B = mod_exp(A, b, p)
    
    print("\nShared key computed by Alice:", key_A)
    print("Shared key computed by Bob:", key_B)
    
    if key_A == key_B:
        print("\nKey exchange successful! Shared secret:", key_A)
    else:
        print("\nKey exchange failed!")


# Run
diffie_hellman()