# Reading from a file
with open("example.txt", "r") as file:
    for line in file:
        print(line)

file = open("/home/CheesiePy/Documents/GitHub/Python_Java_Course/lessons/file.txt", "r")

data = file.read()

print(data)

file.close()

# # Writing to a file
# contents = "hey class!"
# with open("example_copy.txt", "w") as file:
#     for line in contents:
#         file.write(line)