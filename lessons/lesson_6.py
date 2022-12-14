
from random import randint
import time


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