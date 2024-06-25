import string

def cesar_encrypt(message,key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase,string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])#

    encrypted_message = message.lower().translate(cipher)

    return encrypted_message

def cesar_decrypt(encrypted_message, key):

    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = 'this is a silly cybersec project'
key = 3

encrypted_message = cesar_encrypt(message,key)
print(f'Encrypted message: {encrypted_message}')

decypted_message = cesar_decrypt(encrypted_message,key)
print(f'Decrypted message:{decypted_message}')



### 
# str.maketrans Function:

#This function from the string module is used to create a translation table. 
# It takes three arguments:
#source: This specifies the set of characters that will be replaced in the translation process. 
# In our case, it's string.ascii_lowercase, which represents the entire lowercase alphabet ('a', 'b', 'c', ..., 'z').
#replace: This defines the set of characters that will be used to replace the source characters. 
# This is where the Caesar cipher shift comes into play.
# optional third argument: This argument is unused here and can be left empty.                             

#string.ascii_lowercase[shift:]: This part takes a slice of the alphabet starting at the shift position (inclusive) and goes all the way to the end.
#string.ascii_lowercase[:shift]: This slice extracts the part of the alphabet from the beginning (inclusive) up to, but not including, the shift position.
#By concatenating these two slices (string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]), 
# we effectively create a new order for the alphabet where each letter is shifted by the key positions.

