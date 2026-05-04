# Simplified DES (S-DES) Implementation

# Permutation tables
P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
IP  = [4,6,5,8,1,3,2,7]
IP_INV = [5,7,6,1,3,2,8,4]
EP  = [4,1,2,3,2,3,4,1]
P4  = [2,4,3,1]

# S-boxes
S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1:3], 2)
    return format(sbox[row][col], '02b')

# Key generation
def generate_keys(key):
    key = permute(key, P10)
    left, right = key[:5], key[5:]

    left = left_shift(left, 1)
    right = left_shift(right, 1)
    k1 = permute(left + right, P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)
    k2 = permute(left + right, P8)

    return k1, k2

# fK function
def fk(bits, key):
    left, right = bits[:4], bits[4:]

    temp = permute(right, EP)
    temp = xor(temp, key)

    left_sbox = sbox_lookup(temp[:4], S0)
    right_sbox = sbox_lookup(temp[4:], S1)

    temp = permute(left_sbox + right_sbox, P4)
    left = xor(left, temp)

    return left + right

def switch(bits):
    return bits[4:] + bits[:4]

# Encryption
def sdes_encrypt(plaintext, key):
    k1, k2 = generate_keys(key)

    temp = permute(plaintext, IP)
    temp = fk(temp, k1)
    temp = switch(temp)
    temp = fk(temp, k2)

    cipher = permute(temp, IP_INV)
    return cipher

# Decryption
def sdes_decrypt(ciphertext, key):
    k1, k2 = generate_keys(key)

    temp = permute(ciphertext, IP)
    temp = fk(temp, k2)
    temp = switch(temp)
    temp = fk(temp, k1)

    plaintext = permute(temp, IP_INV)
    return plaintext


# Example
key = "1010000010"
plaintext = "11010111"

cipher = sdes_encrypt(plaintext, key)
decrypted = sdes_decrypt(cipher, key)

print("Cipher:", cipher)
print("Decrypted:", decrypted)