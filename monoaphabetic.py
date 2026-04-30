from string import ascii_letters, digits
from random import shuffle

# function is responsible for randomly maping numbers and letters to a new set of numbers and letters. The mapping is one-to-one, 
# meaning each character maps to exactly one other character, and no two characters map to the same character.
def random_monoalphabetic_cipher(pool=None):
    if pool is None:
        pool = ascii_letters + digits
        print("Using default pool of characters: " + pool)
        
    original_pool = list(pool)
    print("Original pool of characters: " + ''.join(original_pool))
    shuffled_pool = list(pool)
    print("Shuffled pool before shuffling: " + ''.join(shuffled_pool))
    
    #this will randomly shuffle the characters in the shuffled_pool list, creating a new random order of characters. This is essential for creating a random monoalphabetic cipher, 
    # as it ensures that each character in the original pool is mapped to a different character in the shuffled pool.
    shuffle(shuffled_pool)
    print("Shuffled pool after shuffling: " + ''.join(shuffled_pool))
    
    return dict(zip(original_pool, shuffled_pool))

#responsible for creating an inverse mapping of the monoalphabetic cipher. 
# It takes a dictionary representing the cipher as input and returns a new dictionary where the keys and values are swapped.
def inverse_monoalphabetic_cipher(cipher):
    inverse_monoalpha = {}
    for key, value in cipher.items():
        inverse_monoalpha[value] = key
    print("Inverse Monoalphabetic Cipher: " + str(inverse_monoalpha))
    return inverse_monoalpha

#responsible for encrypting a message using the provided monoalphabetic cipher.
# It takes a message and a cipher as input, and returns the encrypted message.
def encrypt_with_monoalphabetic_cipher(message, cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(cipher.get(letter, letter))
    print("Encrypted Message: " + ''.join(encrypted_message))   
    return ''.join(encrypted_message)

#responsible for decrypting a message that was encrypted using a monoalphabetic cipher. 
# It takes the encrypted message and the same cipher used for encryption as input, and returns the decrypted message
def decrypt_with_monoalphabetic_cipher(encrypted_message, monoalpha_cipher):
    return encrypt_with_monoalphabetic_cipher(encrypted_message, inverse_monoalphabetic_cipher(monoalpha_cipher))


cipher = random_monoalphabetic_cipher()
print("Generated Monoalphabetic Cipher:", cipher)

encrypted = encrypt_with_monoalphabetic_cipher("Hello World", cipher)
decrypted = decrypt_with_monoalphabetic_cipher(encrypted, cipher)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)