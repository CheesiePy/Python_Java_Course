"""
Lesson 9: Python Collections and Function Behavior

This lesson introduces the basics of Python collections (lists, tuples, sets, dictionaries) and demonstrates pass-by-value and pass-by-reference concepts in Python functions.
"""

# Lists and arrays are the same thing in Python
mylist = [[[], []]]  # Nested list: a list containing empty lists
mylist2 = list("hello world")  # Convert the string to a list of characters
# In a list, there can be duplicates, and the order of items matters

x = 5

print(mylist)  # Print the nested list

# Function to modify the argument, demonstrating pass-by-value
def f(num):
    # Assigning a new value to the argument (does not affect the original variable)
    num = 20
    print(num)  # Print the modified value

f(x)  # Output: 20 (function modifies the local copy)
f(x)  # Output: 20
f(x)  # Output: 20
print(x)  # Output: 5 (x is unchanged because integers are passed by value)

# Function to modify a string, demonstrating pass-by-value
# Strings are immutable in Python, so modifications do not affect the original string
def h(str1):
    str1 += ".end!"  # Concatenate a suffix to the string (creates a new string)

s = "hello"
h(s)  # Attempt to modify the string
print(s)  # Output: hello (s is unchanged because strings are immutable)

# Pass by value vs pass by reference demonstration
# Function to modify a list (lists are mutable, passed by reference)
def g(llist):
    llist.append(15)  # Modify the list by appending a new element

# Modify mylist by adding an element
# Lists are mutable, so changes made within the function persist
# Uncomment the lines below to see how lists are modified by reference
g(mylist)
print(mylist)  # Output: [[[15], []], 15] (list is modified)

# Tuple example
mytuple = (1, 2)  # Tuple: an immutable collection of items
print(type(mytuple))  # Output: <class 'tuple'>

# List example
l1 = [1, 1, 1, 1, 1, 0, 23, 1, 25, 23, 79, 'AG', "Agf"]  # List with duplicates and mixed types

# Set example - order does not matter and no duplicates
myset = set("hey there my python students ! ")  # Convert string to a set of unique characters

# Dictionary example - a collection of key-value pairs
mydict = {
    "key1": "hello",
    "key2": "world"
}

"""
In this lesson, you learned:
1. How Python collections work, including lists, tuples, sets, and dictionaries.
2. The difference between pass-by-value and pass-by-reference in Python functions.
3. How Python handles mutable and immutable data types.

Further Reading:
For more information on Python collections and functions, visit the [Python Documentation](https://docs.python.org/3/tutorial/datastructures.html).
"""
