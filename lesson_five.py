# print() single line comment

"""
multi line comment
"""

import time
from random import randint

counter = 1

for i in "Hello World":
    counter += 1

x = counter != len("Hello World")

# boolean value True or False


data_base = {
    "user" : "KingElad@hotmail.com",
    "password" : "37524018",
}

possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

print(len(possible_chars))
"""
pass "XXXX"
"""

user_name = "KingElad@hotmail.com"

user_pass = ""
user_try = ""


# start = time.time()

# for i in range(100000):
#     print(time.time() - start)


# end = time.time()

# last_result = 2.563169479370117


# print(end - start) 
 

# if (last_result > (end - start)):
#     print("you are faster")


# #brote force attack
# start = time.time()
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
#                                     end = time.time()
#                                     user_pass = user_try
#                                     print("password is: " + user_pass)
#                                     if user_name == data_base["user"] and user_pass == data_base["password"]:
#                                         print("Welcome to the system")
#                                         print("time: " + str(end - start))
#                                     else:
#                                         print(user_pass)                                   


possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
old_adv_point = "Emily_04041984"
adv_point = "Emily_04041984$"

random_og_password = ""
# for i in range(2):
#     random_og_password += possible_chars[(randint(0, len(possible_chars)-1))]

print(random_og_password)

for i in range(1000000):
    random_password = old_adv_point
    start = time.time()

    for j in range(1):
        random_password += possible_chars[(randint(0, len(possible_chars)-1))]

    end = time.time()

    if random_password == adv_point:
        print("success! your password is :" , adv_point)
        print("password is: " + random_password)
        print("number of tries: " + str(i))
        exit()

    print(random_password)
    # print("time: " + str(end - start))