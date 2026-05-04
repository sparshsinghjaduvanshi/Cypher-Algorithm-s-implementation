import numpy as np

#playfair cipher

keyword = "Playfair"
plaintext = "hello"

keyword = keyword.lower().replace('j', 'i')

#remove duplicates from keyword
final_keyword = ""

for letter in keyword:
    if letter not in final_keyword:
        final_keyword += letter
        
# print("Final Keyword: " + final_keyword)

#forming matrix using keyword and the rest of the eltters in the alphabet
matrix = list(final_keyword)
alphabet = [chr(i) for i in range(97, 123)]

# print(matrix)

for letter in alphabet:
    if letter == 'j':
        continue
    elif letter not in matrix:
        matrix.append(letter)
        
matrix = np.array(matrix).reshape(5,5)
# print(matrix)

#pair lapin text letters
plaintext = plaintext.replace(" ","")
plaintext_pairs = []


i = 0
while i < len(plaintext):
    # case 1: last character
    if i == len(plaintext) - 1:
        plaintext_pairs.append(plaintext[i] + 'x')
        i += 1
    
    # case 2: same letters
    elif plaintext[i] == plaintext[i+1]:
        plaintext_pairs.append(plaintext[i] + 'x')
        i += 1
    
    # case 3: normal pair
    else:
        plaintext_pairs.append(plaintext[i] + plaintext[i+1])
        i += 2

print("Plaintext Pairs: " + str(plaintext_pairs))

#encryption
ciphertext = ""

for pair in plaintext_pairs:
    pair_handled = False
    
    #same row
    for row in range(0, 5):
        current_row = matrix[row,:]
        
        if pair[0] in matrix[row,:] and pair[1] in matrix[row, :]:
            first_letter_index = list(current_row).index(pair[0])
            second_letter_index = list(current_row).index(pair[1])
            
            ciphertext += matrix[row, (first_letter_index + 1)% 5]
            ciphertext += matrix[row, (second_letter_index + 1)% 5]
            pair_handled = True
            break
    if pair_handled:
        continue
        
    #same column
    for col in range(0, 5):
        current_col = matrix[:,col]
        if pair[0] in current_col and pair[1] in current_col:
            first_letter_index = list(current_col).index(pair[0])
            second_letter_index = list(current_col).index(pair[1])
    
            ciphertext += matrix[(first_letter_index + 1)% 5, col]
            ciphertext += matrix[(second_letter_index + 1)% 5, col]
            pair_handled = True
            break
    if pair_handled:
        continue
    
    #neither same col or row
    first_letter_coord = np.where(matrix== pair[0])
    second_letter_coord = np.where(matrix== pair[1])
    
    #first letter replacement
    ciphertext += matrix[first_letter_coord[0][0], second_letter_coord[1][0]]
    #second letter replacement
    ciphertext += matrix[second_letter_coord[0][0], first_letter_coord[1][0]]
    

    print(f"Current pair: {pair}")
            
print(matrix)
print(ciphertext)