"""
Lesson 6: Password Guessing using Random Characters

This lesson focuses on generating passwords using random characters to simulate a brute force guessing approach.
"""

# Importing necessary modules
from random import randint
import time

# Defining possible characters for password generation
possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

# Original and target passwords
old_adv_point = "Emily_04041984"
adv_point = "Emily_04041984$"

# Generating a random original password (for demonstration purposes)
random_og_password = ""
# Uncomment the loop below to generate a two-character random password
# for i in range(2):
#     random_og_password += possible_chars[(randint(0, len(possible_chars)-1))]

print(random_og_password)  # Print the generated password (currently empty)

# Attempt to guess the password by appending random characters
for i in range(1000000):  # Loop to simulate password guessing
    random_password = old_adv_point  # Start with the original part of the password
    start = time.time()  # Start timing

    # Append one random character from the possible characters
    for j in range(1):
        random_password += possible_chars[(randint(0, len(possible_chars)-1))]

    end = time.time()  # End timing

    # Check if the generated password matches the target password
    if random_password == adv_point:
        print("Success! Your password is:", adv_point)
        print("Password found: " + random_password)
        print("Number of tries: " + str(i))
        exit()  # Exit the program once the password is found

    # Print the current random password attempt
    print(random_password)
    # Uncomment the line below to print the time taken for each attempt
    # print("Time taken: " + str(end - start))

"""
In this lesson, you learned:
1. How to use random character generation to simulate password guessing.
2. The inefficiency of trying to guess passwords through random combinations.
3. How the `time` module can be used to measure the duration of each password attempt.

Note: This type of password guessing approach is highly inefficient and insecure. It is used here purely for educational purposes to understand the nature of brute force attacks.
"""