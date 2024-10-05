"""
Lesson 3: Loops and Collections

Part 1: Loops
Part 2: Collections
"""

# Part 1: Loops

# For Loop Example
name = "TomBarhava"
# len(string) returns the number of characters in the string
# len(list) returns the number of elements in the list

# Iterate through each character in the string 'name'
for i in name:  # 'i' holds the value of each character in the string
    print(i)

print("-----------------")

# Using range() function
for i in range(10):  # Outputs numbers from 0 to 9
    print(i)

# Iterating through the indices of the string 'name'
for i in range(len(name)):  # Iterates from 0 to len(name) - 1
    if i % 2 == 0:  # Check if the index is even
        print(i, end=" ")
        print(name[i])  # Print the character at the current index

# While Loop Example
# While loop keeps executing as long as the condition is True

# user_input = ""
# while user_input != "exit":
#     user_input = input("Enter a number: ")
#     if user_input.isdigit():  # Check if the input is a digit
#         for i in range(int(user_input)):
#             print(i)
#     else:
#         print("You didn't enter a number")
# print("You exited the program")

# Part 2: Collections

# Lists and Sets
mylist = []  # List: Order matters, duplicates are allowed
myset = set()  # Set: Order does not matter, duplicates are not allowed

# Examples of lists
mylist = [1, 2, 3]
mylist2 = [3, 2, 1]
print(mylist == mylist2)  # Output: False (Order matters in lists)

# Examples of sets
myset = {1, 2, 3}
myset2 = {3, 2, 1}
myset3 = {2, "may", 4, 8, 1}

# Union of sets
myset4 = myset.union(myset3)
print(myset4)  # Combines all unique elements from both sets

# Intersection of sets
myset5 = myset.intersection(myset3)
print(myset5)  # Elements that are common in both sets

# Example of a while loop with a counter
counter = 0
while counter < 500:
    counter += 1
    print(myset3)

# Tuple Example
# Tuples are immutable collections
# Example:
a = 5
b = 7
mytuple = (a, b)
print(mytuple)  # Output: (5, 7)
a = 8  # Changing 'a' does not affect 'mytuple'
print(mytuple[0], mytuple[1])  # Output: 5 7

# Dictionary Example
# Dictionaries store key-value pairs
person = {"name": "Tom", "age": 13, "height": 180, "weight": 70}
print(person.values())  # Output: dict_values(['Tom', 13, 180, 70])

# Matrix Example
# Creating a 9x9 matrix filled with zeros
size = 9
matrix = []
for i in range(size):  # This loop runs 'size' times (9 times)
    matrix.append([])
    for j in range(size):  # This loop runs 'size' times for each row
        matrix[i].append(0)
        print(matrix[i][j], end=" ")
    print()  # Newline after each row

# Homework: Create Diagonal Patterns in a Matrix
# Diagonal Pattern 1
# X 0 0 0 0 0 0 0 0
# 0 X 0 0 0 0 0 0 0
# 0 0 X 0 0 0 0 0 0
# ...
size = 9
for row in range(size):
    for col in range(size):
        if row == col:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()

# Diagonal Pattern 2 (Reverse Diagonal)
# 0 0 0 0 0 0 0 0 V
# 0 0 0 0 0 0 0 V 0
# 0 0 0 0 0 0 V 0 0
# ...
for row in range(size):
    for col in range(size):
        if row + col == size - 1:
            print("V", end=" ")
        else:
            print("0", end=" ")
    print()

# Complex Pattern
# X X X X X X X X X
# X V 0 0 0 0 0 V X
# X 0 V 0 0 0 V 0 X
# ...
for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("X", end=" ")
        elif row == col:
            print("V", end=" ")
        elif row + col == size - 1:
            print("V", end=" ")
        else:
            print("0", end=" ")
    print()

# Scalar Multiplication Example
# Create a grid with a custom height and width
scalar = 1
height = 9
width = 16
for row in range(height * scalar):
    for col in range(width * scalar):
        if row == 0:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()

# Additional Homework Pattern
# X 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 X 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 X 0 0 0 0 0 0 0 0 0 0 0
# ...
for row in range(height):
    for col in range(width):
        if row * 2 == col:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()