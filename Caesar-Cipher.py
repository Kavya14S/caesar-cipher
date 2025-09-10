# Caesar Cipher
def encrypt(plain_text,key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for letter in plain_text:
        if letter in letters:
            letter_index = letters.index(letter)
            cipher_index = (letter_index+key)%26
            cipher += letters[cipher_index]
        else :
            cipher += letter
    return cipher
def decrypt(caesar_text, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    plain = ""
    for letter in caesar_text :
        if letter in letters:
            letter_index = letters.index(letter)
            plain_index = (letter_index - key) % 26
            plain += letters[plain_index]
        else:
            plain += letter
    return plain

operation = input("Type 'encrypt' for encryption, Type 'decrypt' for decryption : ")
if operation == "encrypt":
    plain_text = input("Type your message : ")
    key = int(input("Type your key : "))
    print("Here's the encrypted result : ",encrypt(plain_text,key))
elif operation == "decrypt" :
    caesar_text = input("Type your message : ")
    key = int(input("Type your key : "))
    print("Here's the decrypted result : ",decrypt(caesar_text, key))