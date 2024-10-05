"""
Lesson 12: File Handling in Python

This lesson covers reading from and writing to files using Python. It also demonstrates the importance of closing files and how to use context managers to handle files efficiently.
"""

# Reading from a file
# Open the file "example.txt" in read mode ('r')
# Using a context manager to automatically close the file after reading
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Print each line, stripping extra whitespace and newline characters

# Manually opening a file for reading
file = open("/home/CheesiePy/Documents/GitHub/Python_Java_Course/lessons/file.txt", "r")

# Reading all the contents of the file at once
data = file.read()
print(data)  # Print the entire content of the file

# Close the file to free resources
file.close()

# Writing to a file
# Defining the content to be written to a new file
contents = "hey class!"
# Open "example_copy.txt" in write mode ('w') to write the contents
# Using a context manager to automatically handle closing the file
with open("example_copy.txt", "w") as file:
    for line in contents:
        file.write(line)  # Write each character from the string to the file

# Appending to a file
# Open "example_copy.txt" in append mode ('a') to add more content
with open("example_copy.txt", "a") as file:
    file.write("\nWelcome to Python file handling!")  # Append a new line to the existing file

# Reading a file line by line into a list
with open("example.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    print(lines)  # Print the list of lines

# Writing multiple lines to a file
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multi_lines.txt", "w") as file:
    file.writelines(lines_to_write)  # Write multiple lines to the file at once

# Handling file exceptions
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())  # Attempt to read a file that may not exist
except FileNotFoundError:
    print("The file does not exist. Please check the file path.")

# Using 'r+' mode to read and write to a file
# 'r+' allows both reading and writing without truncating the file
with open("example_copy.txt", "r+") as file:
    print("Initial content:")
    print(file.read())  # Read the current content
    file.write("\nAdding new content using r+ mode.")  # Write new content without deleting existing content

"""
In this lesson, you learned:
1. How to read from a file using `open()` and context managers (`with` statement).
2. How to write to a file and the difference between read ('r'), write ('w'), and append ('a') modes.
3. How to handle exceptions, such as attempting to open a non-existent file.
4. The importance of closing a file to free up system resources and how to use context managers to do this automatically.
5. How to use additional file modes like 'r+' to read and write to files simultaneously.

Further Reading:
For more information on file handling in Python, visit the [Python Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
"""
