## ex1
# max = 0
# min = 0
# command = ""
# zero_flag = True
# while command.lower() != "quit":
    
#     user_input = input("Please Enter a number or quit to exit the program: ")

#     if user_input.lower() == "quit":
#         break
#     try:
#         user_input = int(user_input)
#     except:
#         print("invalid input")

#     if user_input > max:
#         max = user_input

#     if user_input < min or (zero_flag == True):
#         min = user_input
#         zero_flag = False

    
# print("the maximun:" , max)
# print("the minimum:", min)



class BankAccunt():

    def __init__(self, first_deposit=0, od_flag=False, fee=0.5):
        self.balance = first_deposit
        self.overdraft = od_flag
        self.fee = fee

    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
            self.balance -= self.fee

    def withdraw(self, amount):
        if(amount < 0):
            return -1
        if(self.balance < amount and self.overdraft == False):
            print(f"you can withdraw {self.balance}")
            return -1

        self.balance -= amount
        self.balance -= self.fee

    


bank_account = BankAccunt(1000)
bank_account.deposit(-100)
bank_account.withdraw(2200)


print(bank_account.balance)














