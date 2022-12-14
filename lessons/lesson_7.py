# Caesar cipher 

##

# The string to be encrypted/decrypted


# ord()  - 

#print(ord('a')) # ord return a number that represent the value of the unicode 

# message = "c"
# key = 3
# encrypted_m = ""

# n_letter = 26
# my_letter = "z" # -> [97 ,122] (lower case)

# # [0, 25] # 26 natural numbers 

# n = ord(my_letter) # -> (n - 97 + key) % 26

# el = (n - 97 + key) % 26

# print(el)
# print(chr(el + 97))



# my_letter2 = "A"# -> [65 , 90]  (upper case)



# ## encryption
# print("-----------------------------")
# for i in message:
#     encrypted_m += str(ord(i) - key) + " "

# print("after encryp: " , encrypted_m)

# print("-----------------------------")


# #decrypyion
# decrypted_m = ""
# for i in encrypted_m.split():
#     decrypted_m += chr(int(i))

# print("decrypted: ", decrypted_m)


def encrypt(text, key):
    # assume text is lower case.
    all_errors = "!@#$%^&*()_+=-1234567890 "
    encrypted = ""
    for i in text:
        if i in all_errors:
            encrypted += i
        elif i.islower():
            encrypted += chr(((ord(i) - 97 + key)% 26) + 97)
        elif i.isupper():
             encrypted += chr(((ord(i) - 65 + key)% 26) + 65)    
    return encrypted


command = ""
while command.lower() != "quit":
    command = input("please enter your command: ")
    dec = command
    enc = encrypt(dec, 4)
    print(enc)



link = "https://en.wikipedia.org/wiki/Caesar_cipher"