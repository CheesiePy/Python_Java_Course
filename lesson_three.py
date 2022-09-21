"""
part1 loops 
part2 collection 
"""

# for loop
name = "TomBarhava"
#len(str) = number of letters in the str
#len(list) = number of elements in the list

# for i in name: # i holds the value of each letter in the string
#     print(i)

# print("-----------------")


# for i in range(10): # -> 0,1,2,3,4,5,6,7,8,9
#     print(i) 


# for i in range(len(name)): # 0, -> len(name)-1
#     if i % 2 == 0:
#         print(i, end=" ")
#         print(name[i])


# while loop

# while condition:
#     do something

# user_input = ""
# while user_input != "exit":
#     user_input = input("Enter a number: ")
#     if user_input.isdigit():
#         for i in range(int(user_input)):
#             print(i)
#     else:
#         print("You didn't enter a number")
# print("you exited the program")

mylist = [] # order matters, we can have duplicates
myset = {}  # order doesn't matter, we can't have duplicates

mylist = [1,2,3]
mylist2 = [3,2,1]
# print(mylist == mylist2)


# myset = {1,2,3} 
# myset2 = {3,2,1}
# myset3 = {2, "may", 4, 8,1}
# myset4 = myset.union(myset3)
# print(myset4)

# myset5 = myset.intersection(myset3)
# print(myset5)




# print(myset2)
# print(myset == myset2)

counter = 0
# while counter < 500:
#     counter += 1
#     print(myset3)


# condish1 = True
# condish2 = False



# A  = {1, 2, 3}
# B  = {3, 4, 5}
# C = A.intersection(B) 
# print(C)
# D = A.union(B)
# print(D)


# if 1 in A and B:
#     print("i is in A")
# a = 5
# b = 7
# mytuple = (a,b)
# print(mytuple)
# a = 8
# print(mytuple[0] , mytuple[1])

# person  = { "name": 13, "age": 13, "height":13, "weight": 13}
# print(person.values())


size = 9
matrix = []
for i in range(size): # this loop will run 3 times 
    matrix.append([])
    for j in range(size): # this loop will run 3 X 3 times -> 9 times
        matrix[i].append(0)
        print(matrix[i][j], end=" ")
    print() 

 
 