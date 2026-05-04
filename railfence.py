# import numpy as np

# key = 4312567
# plaintext = "attack postponed until two am"

# def rail_fence(key: int, plaintext: str):
#     #prepping variables
#     pliantext = plaintext.replace(" ","")
#     key_list = [int(i) for i in str(key)]
    
#     sorted_key_list = [int(i) for i in str(key)]
#     sorted_key_list.sort()
    
#     remainder = len(plaintext)% len(key_list)
#     if(len(plaintext) % len(key_list) > 0):
#         #appending letters starting from the end(z <-) to make a full rectangle
#         no_of_letters_to_add = len(key_list) - remainder
        
#         # eg, no_of_letters_to_add = 1, 123-1 = 122, 121, 122
#         for i in range(123 - no_of_letters_to_add,123):
#             plaintext += chr(i)
            
#     #encryption 
#     cols = len(key_list)
#     rows = len(plaintext)
    
#     print(f"Key length/cols: {cols}")
#     print(f"Plaintext length: {len(plaintext)}")
#     print(f"rows: {rows}")
#     encryption_rectangle = np.array([letter for letter in plaintext]).reshape(rows, cols)
#     print(encryption_rectangle)

# rail_fence(key, plaintext)
        

# railfence cipher    

def rail_fence_encrypt(text, key):
    # ---- validation ----
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")

    if key < 2:
        raise ValueError("Key must be >= 2")

    if not isinstance(text, str):
        raise ValueError("Plaintext must be a string")

    text = text.lower().strip()

    if len(text) == 0:
        raise ValueError("Plaintext cannot be empty")

    # keep only alphabets
    text = ''.join(c for c in text if c.isalpha())

    # ---- encryption ----
    rails = ['' for _ in range(key)]
    
    row = 0
    direction = 1

    for char in text:
        rails[row] += char

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rails)

# test
plaintext = "attack postponed"
key = 3

cipher = rail_fence_encrypt(plaintext, key)
print("Ciphertext:", cipher)