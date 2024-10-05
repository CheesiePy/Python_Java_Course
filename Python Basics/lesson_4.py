"""
Lesson 4: Matrix Patterns and Homework

This lesson covers generating different patterns using loops and matrices.
"""

# Part 1: Creating a 9x9 Matrix Filled with Zeros
# The goal is to create a 9x9 matrix and fill it with zeros

size = 9
matrix = []
for i in range(size):  # This loop runs 'size' times (9 times)
    matrix.append([])  # Add a new row to the matrix
    for j in range(size):  # This loop runs 'size' times for each row
        matrix[i].append(0)  # Append 0 to the current row
        print(matrix[i][j], end=" ")  # Print each element in the row
    print()  # Newline after each row

# Homework Part 1: Create a Diagonal Pattern in a 9x9 Matrix
# X 0 0 0 0 0 0 0 0
# 0 X 0 0 0 0 0 0 0
# 0 0 X 0 0 0 0 0 0
# 0 0 0 X 0 0 0 0 0
# 0 0 0 0 X 0 0 0 0
# 0 0 0 0 0 X 0 0 0
# 0 0 0 0 0 0 X 0 0
# 0 0 0 0 0 0 0 X 0
# 0 0 0 0 0 0 0 0 X

size = 9
for row in range(size):
    for col in range(size):
        if row == col:
            print("X", end=" ")  # Print 'X' when row equals column (diagonal)
        else:
            print("0", end=" ")  # Print '0' elsewhere
    print()  # Newline after each row

# Homework Part 2: Create a Reverse Diagonal Pattern in a 9x9 Matrix
# 0 0 0 0 0 0 0 0 V
# 0 0 0 0 0 0 0 V 0
# 0 0 0 0 0 0 V 0 0
# 0 0 0 0 0 V 0 0 0
# 0 0 0 0 V 0 0 0 0
# 0 0 0 V 0 0 0 0 0
# 0 0 V 0 0 0 0 0 0
# 0 V 0 0 0 0 0 0 0
# V 0 0 0 0 0 0 0 0

for row in range(size):
    for col in range(size):
        if row + col == size - 1:
            print("V", end=" ")  # Print 'V' when row + col equals size - 1 (reverse diagonal)
        else:
            print("0", end=" ")  # Print '0' elsewhere
    print()  # Newline after each row

# Homework Part 3: Complex Pattern in a 9x9 Matrix
# X X X X X X X X X
# X V 0 0 0 0 0 V X
# X 0 V 0 0 0 V 0 X
# X 0 0 V 0 V 0 0 X
# X 0 0 0 V 0 0 0 X
# X 0 0 V 0 V 0 0 X
# X 0 V 0 0 0 V 0 X
# X V 0 0 0 0 0 V X
# X X X X X X X X X

for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("X", end=" ")  # Print 'X' for the border
        elif row == col:
            print("V", end=" ")  # Print 'V' for the main diagonal
        elif row + col == size - 1:
            print("V", end=" ")  # Print 'V' for the reverse diagonal
        else:
            print("0", end=" ")  # Print '0' elsewhere
    print()  # Newline after each row

# Part 2: Scalar Multiplication Example
# Creating a grid with a custom height and width, using scalar multiplication
scalar = 1
height = 9
width = 16
for row in range(height * scalar):
    for col in range(width * scalar):
        if row == 0:
            print("X", end=" ")  # Print 'X' for the first row
        else:
            print("0", end=" ")  # Print '0' for all other rows
    print()  # Newline after each row

# Homework Bonus: Diagonal Pattern with Increasing Gaps
# X 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 X 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 X 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 X 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 X 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 X 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 X 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 X 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 X

for row in range(height):
    for col in range(width):
        if row * 2 == col:
            print("X", end=" ")  # Print 'X' when column index is twice the row index
        else:
            print("0", end=" ")  # Print '0' elsewhere
    print()  # Newline after each row