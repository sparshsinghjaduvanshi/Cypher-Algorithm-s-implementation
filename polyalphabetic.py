alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# polyalphabetic
message = input("Enter the message to encrypt: ")
message = message.lower()

password = input("Enter the password for the cipher: ")
password = password.lower()
password = password*len(message)

cipherText = ""

count = 0
for letter in message:
    if letter in alphabet:
        #define shift value based on the corresponding letter in the password
        shift = alphabet.index(password[count])
        
        #define the index of the letter in the alphabet
        letter_index = alphabet.index(letter)
        cipherLetter = alphabet[(letter_index + shift)%26]
        cipherText = cipherText + cipherLetter
        count = count+ 1
    else:
        cipherText = cipherText + letter
    
print("The encrypted message is:", cipherText)