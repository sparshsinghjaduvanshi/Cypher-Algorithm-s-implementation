from math import gcd
import numpy as np

#text-> numbers
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

#numbers -> text
def numbers_to_text(numbers):
    return ''.join(chr(int(num) + ord('A')) for num in numbers)

#hill cipher encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext_numbers = text_to_numbers(plaintext)
    n = key_matrix.shape[0]
    
    # Pad plaintext if necessary
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(0)  # Padding with 'A' (0)
    
    ciphertext_numbers = []
    
    for i in range(0, len(plaintext_numbers), n):
        block = np.array(plaintext_numbers[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(encrypted_block)
    
    return numbers_to_text(ciphertext_numbers)

#hill cipher decryption

def mod_matrix_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix))) % modulus
    
    if gcd(det, modulus) != 1:
        raise ValueError("Matrix is not invertible under mod {}".format(modulus))
    
    det_inv = pow(det, -1, modulus)

    # Cofactor matrix
    cofactors = np.zeros(matrix.shape)
    n = matrix.shape[0]

    for r in range(n):
        for c in range(n):
            minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
            cofactors[r][c] = ((-1) ** (r + c)) * int(round(np.linalg.det(minor)))

    adjugate = cofactors.T
    return (det_inv * adjugate) % modulus


def hill_decrypt(ciphertext, key_matrix):
    ciphertext_numbers = text_to_numbers(ciphertext)
    n = key_matrix.shape[0]

    key_matrix_inv = mod_matrix_inverse(key_matrix, 26)

    plaintext_numbers = []

    for i in range(0, len(ciphertext_numbers), n):
        block = np.array(ciphertext_numbers[i:i+n])
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        plaintext_numbers.extend(decrypted_block)

    return numbers_to_text(plaintext_numbers)
plainText = "HelloWorld"
keyMatrix = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])
cipherText = hill_encrypt(plainText, keyMatrix)
print("Encrypted Message:", cipherText)

decryptedText = hill_decrypt(cipherText, keyMatrix)
print("Decrypted Message:", decryptedText)
