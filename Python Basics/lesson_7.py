"""
Lesson 7: Caesar Cipher Encryption

This lesson introduces the Caesar Cipher, one of the simplest and most well-known encryption techniques.
"""

# The Caesar Cipher
# The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

# ord() - returns the Unicode code point for a given character
# chr() - returns the character that represents a given Unicode code point

# Example Usage of ord() and chr()
# print(ord('a'))  # ord returns a number that represents the value of the Unicode character ('a' -> 97)

# Example: Encrypting and Decrypting a Single Character
message = "c"
key = 3
encrypted_m = ""

n_letter = 26  # Number of letters in the alphabet
my_letter = "z"  # 'z' in lowercase corresponds to Unicode values between [97, 122]

# Calculation for shifting the letter 'z' by the key value
n = ord(my_letter)  # Get Unicode value of 'my_letter'
el = (n - 97 + key) % 26  # Calculate the new position after shifting by key

# Print the encrypted value
print(el)
print(chr(el + 97))  # Convert back to character

my_letter2 = "A"  # 'A' in uppercase corresponds to Unicode values between [65, 90]

# Encryption Example
print("-----------------------------")
for i in message:
    encrypted_m += str(ord(i) - key) + " "

print("After encryption:", encrypted_m)
print("-----------------------------")

# Decryption Example
decrypted_m = ""
for i in encrypted_m.split():
    decrypted_m += chr(int(i))

print("Decrypted:", decrypted_m)

# Encrypt Function
def encrypt(text, key):
    # Assume text can be both upper and lower case.
    all_errors = "!@#$%^&*()_+=-1234567890 "  # Characters that should not be encrypted
    encrypted = ""
    for i in text:
        if i in all_errors:
            encrypted += i  # Keep special characters and digits unchanged
        elif i.islower():
            encrypted += chr(((ord(i) - 97 + key) % 26) + 97)  # Encrypt lowercase letters
        elif i.isupper():
            encrypted += chr(((ord(i) - 65 + key) % 26) + 65)  # Encrypt uppercase letters
    return encrypted

# Command Loop for User Interaction
command = ""
while command.lower() != "quit":
    command = input("Please enter your command: ")
    dec = command
    enc = encrypt(dec, 4)  # Encrypt the user input with a key of 4
    print(enc)  # Print the encrypted message

# Additional Resource
link = "https://en.wikipedia.org/wiki/Caesar_cipher"
print("Learn more about the Caesar Cipher here:", link)

"""
In this lesson, you learned:
1. How to use the Caesar Cipher to encrypt and decrypt messages.
2. The usage of `ord()` and `chr()` functions for character conversion.
3. How to handle both lowercase and uppercase letters during encryption.
4. The importance of maintaining certain characters unmodified during encryption.

Further Reading:
For more information, visit the [Wikipedia page on Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).
"""