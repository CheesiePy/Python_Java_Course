"""
Lesson 10: Function Operations in Python

This lesson introduces several functions that demonstrate basic operations, including mathematical computations, string manipulation, and greeting functions. Additionally, it explains how functions interact with each other and how they can be combined to solve more complex problems.
"""

# Function that returns a constant value
def f():
    # This function takes no arguments and always returns the integer 7
    return 7

# Function that computes the power of two numbers
def g(x, y):
    # This function returns x raised to the power of y
    return x ** y

# Function that multiplies a string a given number of times
def s(str, num):
    # This function repeats the string 'str' for 'num' times and returns the result
    return str * num

# Function that uses other functions to generate a result
def fgs(str, x, y):
    # This function calls g(x, y) to compute x raised to the power y,
    # then calls s(str, result) to repeat the string 'str' that many times
    return s(str, g(x, y))

# Function that generates a greeting message
def greet(name):
    # This function takes a name and returns a personalized greeting
    # The name is capitalized using the title() method
    return f"Hello {name.title()}, thank you for asking about me!"

# Function that greets all names in an array
def greetAll(name_array):
    # This function takes a list of names and prints a greeting for each one
    for i in name_array:
        print(greet(i))

# Main function to demonstrate the use of other functions
def main():
    # Demonstrates the use of the title() method (no effect here as the result is not assigned)
    name = "Maor"
    name.title()
    
    # Define a list of names (with some duplicates)
    name_array = ["maor", "maor", "maor", "maor", "maor", "matan", "tom", "yair", "elad", "emily", "eliko", "ilay"]
    
    # Convert the list to a set to remove duplicates, then greet all unique names
    uniq_names = set(name_array)
    greetAll(uniq_names)

# Call the main function to execute the program
main()

# Print an empty line
print()

"""
In this lesson, you learned:
1. How to define functions in Python and their basic syntax.
2. How to pass arguments to functions and return values.
3. The difference between using return values and printing directly within a function.
4. How functions can call other functions to perform more complex operations.
5. How to manipulate collections, such as lists and sets, to achieve desired outcomes.

Further Reading:
For more information on Python functions, visit the [Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).
"""
