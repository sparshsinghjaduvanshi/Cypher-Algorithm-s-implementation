#Diffi-Hellman

# def mod_exp(base, exp, mod):
#     result = 1
#     base = base % mod
#     while exp > 0:
#         if exp %2 == 1:
#             result = (result*base)% mod
#         base = (base*base) % mod
#         exp //= 2
#     return result


# def hell_man():
#     p = int(input("Enter a large prime number: "))
#     g = int(input("Enter a function generator: "))
    
    
#     a = int(input("enter a number for A: "))
#     b = int(input("enter a number for B: "))
    
#     A = mod_exp(g, a, p)
#     B = mod_exp(g, b, p)
    
#     print("Public A: ",A)
#     print("Public B: ",B)
    
#     Xa = mod_exp(B, a, p)
#     Xb = mod_exp(A, b, p)
    
#     print("privat A ",Xa)
#     print("privat B ",Xb)
    
#     if Xa == Xb:
#         print("pass")
#     else:
#         print("fail")
        
# hell_man()


#ELGamal
# import random

# def inverse(s, p):
#     inverse = pow(s, -1, p)
#     return inverse

# def key(g, x, p):
#     k = pow(g,x, p)
#     return (p, g, k),x

# def encrypt(M, public_key):
#     p, g, y = public_key
#     k = random.randint(1, p-1)
#     print("random number K: ", k)
#     C1 = pow(g, k, p)
#     C2 = (M * pow(y,k,p)) % p
    
#     return (C1, C2)

# def decrypt(cipher, x, p):
#     C1, C2 = cipher
#     s = pow(C1, x, p)
#     s_inverse = inverse(s,p)
#     D = (C2* s_inverse) %p
#     return D

# def Elgamal():
#     p = int(input("Enter a large prime number: "))
#     g = int(input("Enter a generator function: "))
#     x = int(input("Enter a private key: "))
    
#     public_key, private_key = key(g, x, p)
    
#     M = int(input("Enter a message: "))
    
#     enc = encrypt(M, public_key)    
#     dec = decrypt(enc, private_key, p)
    
#     print(enc)
#     print(dec)
    
# Elgamal()


#rail_fence
# def encrypt(text, key):
#     text = text.lower().strip()
    
#     text = (c for c in text if c.isalpha())
#     rails = ['' for _ in range(key)]
    
#     row = 0
#     distance = 1
    
#     for ch in text:
#         rails[row] += ch
#         if row == 0:
#             distance = 1
#         if row == key-1:
#             distance = -1
#         row += distance
        
#     return ''.join(rails)

# plaintext = "attack postponed"
# key  =3 

# cipher = encrypt(plaintext, key)
# print(cipher)

# Monoalphabetic cipher
from string import ascii_letters, digits
from random import shuffle
def random_monoalphabatic_cipher(pool = None):
    if pool == None:
        pool = ascii_letters + digits
        
    original_pool = list(pool)
    print("Original pool:", ''.join(original_pool))
    shuffled_pool = list(pool)
    
    shuffle(shuffled_pool)
    print("Shuffled pool: ", ''.join(shuffled_pool))
    
    return dict(zip(original_pool, shuffled_pool))
        
def inverse_pool(cipher):
    inverse_pool = {}
    for key, value in cipher:
        inverse_pool[value] = key
        
    print("Inverse pool: ", str(inverse_pool))
    return inverse_pool

    
def encrypt(text, cipher):
    encrypted_message = []
    
    