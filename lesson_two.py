# primitive types 

a = 5.0 ## float
b = 4  ## int
c = "String" ## str
d = True     ## bool





## collections
x = [] # list
# y = () # tuple
# z = {} # set
# map = {x:y} # dict





#print(type(c))

## operators

# + , - ,*, /, %, **, //
# +, * -> str, int, float
# -, /, %, **, // -> int, float

#print(b % 5) # -> 0,1,2,3,4   # modulo 0 -> (n-1)

# box = 81908
 
# while box <= 8:
#     box -= 8
#     print("im in the while loop", box)

# print(box)

# print("im the modulo operator", 81908%8)

# if, elif, else

#if condition:
    # do something

condition = 15 <= 10
condition2 = 15 == int("15")
# print(condition)
# if not condition:
#     print("15 is less than or equal to 10") 

# if condition and condition2:
#     print("both conditions are true")

# if condition or condition2:
#     print("one of the conditions is true")

if not(condition or condition2 and not(condition)):
    print("this is true")

## comparison operators // comparators a == b, a != b, a < b, a > b, a <= b, a >= b
# ==, !=, >, <, >=, <=



# for loop
# for i in range(31):
#     if i % 2 == 0:
#         print(i, "is even") # i can't be here 
#     elif i % 3 == 0:
#         print(i, "is divisible by 3") # and here at the time
#     else: # else is bound to the closest if
#         print(i, "is odd")

long_last_name = "BenimovichLiel"
this_is_a_list = ["may", "gil", "maor", "tom", "elad",5, True, 6.1]

print(this_is_a_list[0]) # -> may
print(this_is_a_list[1]) # -> gil
print(this_is_a_list[2]) # -> maor
print(this_is_a_list[-1]) # -> 6.1
print(this_is_a_list[-4]) #
print(this_is_a_list[4]) #


# print(type(this_is_a_list))

# for i in long_last_name:
#     print(i)

# for index in range(len(long_last_name)):
#     print(long_last_name[index])

# print("Ilay", "Yair", sep="^_^", end="+$")
"""
 1. print every element with "Good Morning" in front of it ["may", "gil", "maor", "tom", "elad"]
#example: "Good Morning may"
          "Good Morning gil"
          "Good Morning maor"
          "Good Morning tom"
          "Good Morning elad"
 2. print every element with "Good Night" in front of it in reverse order
          "Good Night elad"
          "Good Night tom"
          "Good Night maor"
          "Good Night gil"
          "Good Night may"
3. print intertwine of the names in the list BONUS
example: "Good Morning may"
         "Good Night elad"
         "Good Morning gil"
         "Good Night tom"

"""
print(500%7)