
# size = 9
# matrix = []
# for i in range(size): # this loop will run 3 times 
#     matrix.append([])
#     for j in range(size): # this loop will run 3 X 3 times -> 9 times
#         matrix[i].append(0)
#         print(matrix[i][j], end=" ")
#     print() 


""" home work:
X 0 0 0 0 0 0 0 0 
0 X 0 0 0 0 0 0 0 
0 0 X 0 0 0 0 0 0 
0 0 0 X 0 0 0 0 0 
0 0 0 0 X 0 0 0 0 
0 0 0 0 0 X 0 0 0 
0 0 0 0 0 0 X 0 0 
0 0 0 0 0 0 0 X 0 
0 0 0 0 0 0 0 0 X 
"""
# size = 9
# for row in range(size):
#     for col in range(size):
#         if row == col:
#             print("X", end=" ")
#         else:
#             print("0", end=" ")    
#     print()

""" home work:
0 0 0 0 0 0 0 0 V 
0 0 0 0 0 0 0 V 0 
0 0 0 0 0 0 V 0 0 
0 0 0 0 0 V 0 0 0 
0 0 0 0 V 0 0 0 0 
0 0 0 V 0 0 0 0 0 
0 0 V 0 0 0 0 0 0 
0 V 0 0 0 0 0 0 0 
V 0 0 0 0 0 0 0 0 
"""

"""
homework:
X X X X X X X X X 
X V 0 0 0 0 0 V X 
X 0 V 0 0 0 V 0 X 
X 0 0 V 0 V 0 0 X 
X 0 0 0 V 0 0 0 X 
X 0 0 V 0 V 0 0 X 
X 0 V 0 0 0 V 0 X 
X V 0 0 0 0 0 V X 
X X X X X X X X X 
"""
size = 9
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()

 

# scalar = 1
# height = 9
# width = 16
# for row in range(height*scalar):
#     for col in range(width*scalar):
#         if row == 0:
#             print("X", end=" ")
#         else:     
#             print("0", end=" ")  
#     print()



""" homework bonus

X 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 X 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 X 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 X 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 X 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 X 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 X 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 X 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 X
""" 