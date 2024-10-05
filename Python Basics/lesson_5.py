"""
Lesson 5: Brute Force and Timing Analysis

This lesson introduces how to use loops for brute force password cracking and timing analysis.
"""

# Print statement and comments
# print() is used for single line comments

"""
Multi-line comment
"""

# Importing required modules
import time
from random import randint

# Initializing a counter
counter = 1

# Iterating through each character in the string "Hello World"
for i in "Hello World":
    counter += 1

# Comparing counter with the length of "Hello World"
x = counter != len("Hello World")

# Boolean value: True or False

# Dictionary to represent a simple database
data_base = {
    "user": "KingElad@hotmail.com",
    "password": "37524018",
}

# Possible characters for password generation
possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

# Printing the length of possible characters
print(len(possible_chars))  # Output: 72

"""
Password example: "XXXX"
"""

# User credentials
user_name = "KingElad@hotmail.com"
user_pass = ""
user_try = ""

# Timing example
# Measuring the time taken by a loop execution
# start = time.time()
# for i in range(100000):
#     print(time.time() - start)
# end = time.time()

# Last recorded result for comparison
last_result = 2.563169479370117

# Printing the total time taken
# print(end - start)

# Comparing last result with current timing
# if last_result > (end - start):
#     print("You are faster")

# Brute Force Attack Example
# Attempting to crack the password using nested loops
start = time.time()
for i in range(10):  # Loop for the first digit (0-9)
    for j in range(10):  # Loop for the second digit (0-9)
        for k in range(10):  # Loop for the third digit (0-9)
            for w in range(10):  # Loop for the fourth digit (0-9)
                for q in range(10):  # Loop for the fifth digit (0-9)
                    for e in range(10):  # Loop for the sixth digit (0-9)
                        for d in range(10):  # Loop for the seventh digit (0-9)
                            for c in range(10):  # Loop for the eighth digit (0-9)
                                # Concatenate digits to form a password attempt
                                user_try = str(i) + str(j) + str(k) + str(w) + str(q) + str(e) + str(d) + str(c)
                                # Check if the generated password matches the actual password
                                if user_try == data_base["password"]:
                                    end = time.time()
                                    user_pass = user_try
                                    print("Password is: " + user_pass)
                                    # Check if both username and password match the database
                                    if user_name == data_base["user"] and user_pass == data_base["password"]:
                                        print("Welcome to the system")
                                        print("Time taken: " + str(end - start))
                                    else:
                                        print(user_pass)  # Print incorrect password attempt
"""
In this lesson, you learned:
1. How to use loops for brute force password cracking.
2. How to use the `time` module to measure the performance of code execution.
3. The importance of nested loops in generating password attempts.
Note: Brute force attacks are highly inefficient and are used here for educational purposes only.
"""