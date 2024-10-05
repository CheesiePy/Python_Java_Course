"""
Lesson 13: Recursion in Python

This lesson covers the concept of recursion, which occurs when a function calls itself. Recursion is often used to solve problems that can be divided into similar subproblems, such as calculating factorials, Fibonacci numbers, and summing the digits of a number. Each recursive function must have an exit condition to avoid infinite loops.
"""

# Simple recursion example: Infinite recursion without an exit condition
def f():
    print("hello")
    f()  # This is a recursive call that will continue indefinitely (Stack overflow)

# Recursion with an exit condition
# Recursion must have an exit condition to prevent infinite looping
def f(n):
    if n == 0:
        return  # Base case to stop recursion
    print("hello")
    f(n - 1)  # Recursive call, reducing n each time until it reaches 0

# Example: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1  # Base case: factorial of 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

print(factorial(5))  # Output: 120

# Example: Fibonacci sequence using recursion
def fibonacci(n):
    if n == 1 or n == 2:
        return 1  # Base case: first two Fibonacci numbers are 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case: sum of the previous two Fibonacci numbers

# Uncomment the line below to see the output (note: large values of n can take a long time to compute)
# print(fibonacci(40))

# Example: Sum of digits using recursion
def sum_digits(n):
    if n < 10:
        return n  # Base case: if n is a single digit, return n
    else:
        return n % 10 + sum_digits(n // 10)  # Recursive case: add the last digit to the sum of the remaining digits

print(sum_digits(22222))  # Output: 10

# Example: Custom recursion function with multiple conditions
def fq(n):
    if n < 0:
        return "im at the end"  # Base case: when n is less than 0
    
    fq(n - 1)  # Recursive call to continue until n is less than 0
    if n % 3 == 0 and n % 2 == 0:  # Condition to print numbers divisible by both 3 and 2
        print(n)
    return None

print(fq(88))  # Output: Numbers divisible by both 3 and 2, counting down from 88

"""
In this lesson, you learned:
1. What recursion is and how to implement it in Python.
2. The importance of having an exit condition in a recursive function to avoid infinite recursion.
3. How to use recursion to solve problems such as calculating factorials, Fibonacci numbers, and summing digits.
4. How to use different base cases to handle specific scenarios in recursive functions.

Further Reading:
For more information on recursion in Python, visit the [Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#recursive-functions).
"""
