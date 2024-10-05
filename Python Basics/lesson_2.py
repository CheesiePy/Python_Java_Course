# Primitive Types

a = 5.0  # float
b = 4    # int
c = "String"  # str
d = True  # bool

# Collections
x = []  # list
y = ()  # tuple
z = set()  # set
my_map = {"key": "value"}  # dict

# Print type of a variable
print(type(c))

# Operators
# Arithmetic Operators: +, -, *, /, %, **, //
# +, * -> Can be used with str, int, float
# -, /, %, **, // -> Can be used with int, float

print(b % 5)  # Modulo operation (returns remainder) -> Output: 4 (b = 4)

box = 81908

# While loop example
while box > 8:
    box -= 8
    print("I am in the while loop", box)

print("Final box value:", box)

# Using modulo operator to get remainder
print("Result of modulo operation:", 81908 % 8)

# Conditional Statements (if, elif, else)

condition = 15 <= 10
condition2 = 15 == int("15")

print("Condition 1:", condition)  # Output: False
print("Condition 2:", condition2)  # Output: True

# Example of if-elif-else statement
if not condition:
    print("15 is not less than or equal to 10")

if condition and condition2:
    print("Both conditions are true")

if condition or condition2:
    print("One of the conditions is true")

if not (condition or condition2 and not condition):
    print("This is true")

# Comparison Operators: ==, !=, >, <, >=, <=
# Used to compare values

# For Loop
for i in range(31):
    if i % 2 == 0:
        print(i, "is even")
    elif i % 3 == 0:
        print(i, "is divisible by 3")
    else:
        print(i, "is odd")

# Accessing List Elements
long_last_name = "BenimovichLiel"
this_is_a_list = ["may", "gil", "maor", "tom", "elad", 5, True, 6.1]

print(this_is_a_list[0])  # Output: may
print(this_is_a_list[1])  # Output: gil
print(this_is_a_list[2])  # Output: maor
print(this_is_a_list[-1])  # Output: 6.1
print(this_is_a_list[-4])  # Output: tom
print(this_is_a_list[4])  # Output: elad

# Iterating over strings and lists
for char in long_last_name:
    print(char)

for index in range(len(long_last_name)):
    print(long_last_name[index])

print("Ilay", "Yair", sep="^_^", end="+$")  # Custom separator and end character

# Exercises
# 1. Print every element with "Good Morning" in front of it from this_is_a_list
names_list = ["may", "gil", "maor", "tom", "elad"]
for name in names_list:
    print("Good Morning", name)

# 2. Print every element with "Good Night" in front of it in reverse order
for name in reversed(names_list):
    print("Good Night", name)

# 3. Print intertwine of the names in the list (BONUS)
for i in range(len(names_list) // 2):
    print("Good Morning", names_list[i])
    print("Good Night", names_list[-(i + 1)])

# Printing the remainder when 500 is divided by 7
print(500 % 7)  # Output: 2