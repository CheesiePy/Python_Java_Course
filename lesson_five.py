# print() single line comment

"""
multi line comment
"""

counter = 1

for i in "Hello World":
    counter += 1

x = counter != len("Hello World")

# boolean value True or False


data_base = {
    "user" : "KingElad@hotmail.com",
    "password" : "375",
}

possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

print(len(possible_chars))
"""
pass "XXXX"
"""

user_name = "KingElad@hotmail.com"

user_pass = ""
user_try = ""

# # brote force attack
# for i in range(10): # 10
#     for j in range(10): # 100
#         for k in range(10): # 1000
#             for w in range(10): # 10000
#                 for q in range(10): # 100000
#                     for e in range(10): # 1000000
#                         for d in range(10): # 10000000
#                             for c in range(10): # 100000000
#                                 user_try = str(i) + str(j) + str(k) + str(w) + str(q) + str(e) + str(d) + str(c)
#                                 if user_try == data_base["password"]:
#                                     user_pass = user_try
#                                     print("password is: " + user_pass)
#                                     break


# if user_name == data_base["user"] and user_pass == data_base["password"]:
#     print("Welcome to the system")
# else:
#     print(user_pass)
