
max = 0
min = 0
command = ""
zero_flag = True
while command.lower() != "quit":
    
    user_input = input("Please Enter a number or quit to exit the program: ")

    if user_input.lower() == "quit":
        break
    try:
        user_input = int(user_input)
    except:
        print("invalid input")

    if user_input > max:
        max = user_input

    if user_input < min or (zero_flag == True):
        min = user_input
        zero_flag = False

    


print("the maximun:" , max)
print("the minimum:", min)
