"""
Lesson 11: Looping for Input and Bank Account Class

This lesson introduces a while loop to get user input and demonstrates the implementation of a simple Bank Account class with features like deposit, withdrawal, and handling overdraft.
"""

# Example 1: Finding Maximum and Minimum with User Input
# This loop keeps asking the user for input until they type "quit" to exit
# It tracks the maximum and minimum values entered

max = 0
min = 0
command = ""
zero_flag = True  # Flag to initialize minimum on the first input

while command.lower() != "quit":
    user_input = input("Please Enter a number or quit to exit the program: ")
    print(f"Received input: {user_input}")  # Debug log to track user input

    if user_input.lower() == "quit":
        break
    try:
        user_input = int(user_input)  # Try to convert input to an integer
    except:
        print("Invalid input")
        continue  # Skip to the next iteration if input is invalid

    # Update maximum value if applicable
    if user_input > max:
        print(f"Updating max from {max} to {user_input}")  # Debug log to track max update
        max = user_input

    # Update minimum value if applicable
    if user_input < min or zero_flag:
        print(f"Updating min from {min} to {user_input}")  # Debug log to track min update
        min = user_input
        zero_flag = False  # Disable zero_flag after the first valid input

# Print the results
print("The maximum:", max)
print("The minimum:", min)

# Bank Account Class Example
class BankAccount():
    def __init__(self, first_deposit=0, od_flag=False, fee=0.5):
        # Initialize the bank account with an optional first deposit, overdraft flag, and transaction fee
        self.balance = first_deposit  # Set the initial balance
        self.overdraft = od_flag  # Indicates if overdraft is allowed
        self.fee = fee  # Transaction fee for each operation
        print(f"BankAccount created with balance: {self.balance}, overdraft: {self.overdraft}, fee: {self.fee}")  # Debug log to track account creation

    def deposit(self, amount):
        # Deposit money into the account, deducting a transaction fee
        print(f"Attempting to deposit: {amount}")  # Debug log to track deposit attempt
        if amount > 0:
            self.balance += amount  # Add the deposit amount to the balance
            self.balance -= self.fee  # Deduct the transaction fee
            print(f"Deposit successful. New balance: {self.balance}")  # Debug log to track successful deposit
        else:
            print("Deposit amount must be positive.")  # Ensure only positive amounts are deposited

    def withdraw(self, amount):
        # Withdraw money from the account, checking conditions for overdraft and valid amount
        print(f"Attempting to withdraw: {amount}")  # Debug log to track withdrawal attempt
        if amount < 0:
            print("Withdrawal amount must be positive.")  # Ensure only positive amounts are withdrawn
            return -1  # Invalid withdrawal amount
        if self.balance < amount and not self.overdraft:
            # If balance is insufficient and overdraft is not allowed, restrict withdrawal
            print(f"You can withdraw up to {self.balance}")
            return -1

        self.balance -= amount  # Deduct the withdrawal amount from the balance
        self.balance -= self.fee  # Deduct the transaction fee
        print(f"Withdrawal successful. New balance: {self.balance}")  # Debug log to track successful withdrawal

    def enable_overdraft(self):
        # Enable overdraft for the account
        self.overdraft = True
        print("Overdraft enabled.")  # Debug log to track overdraft status

    def disable_overdraft(self):
        # Disable overdraft for the account
        self.overdraft = False
        print("Overdraft disabled.")  # Debug log to track overdraft status

    def get_balance(self):
        # Return the current balance of the account
        print(f"Current balance: {self.balance}")  # Debug log to track balance inquiry
        return self.balance

    def __str__(self):
        # String representation of the bank account
        return f"BankAccount(balance={self.balance}, overdraft={'enabled' if self.overdraft else 'disabled'})"

# Create a bank account instance with an initial deposit of 1000
bank_account = BankAccount(1000)

# Attempt to deposit a negative amount (invalid operation)
bank_account.deposit(-100)

# Attempt to withdraw an amount greater than the balance (without overdraft)
bank_account.withdraw(2200)

# Print the current balance
print(bank_account.balance)  # Output the current balance after transactions

# Enable overdraft and try withdrawing again
bank_account.enable_overdraft()
bank_account.withdraw(2200)
print(bank_account.balance)  # Output the balance after allowing overdraft

# Print the bank account details
print(bank_account)  # Output the details of the bank account

"""
In this lesson, you learned:
1. How to use a while loop to repeatedly get user input and find maximum and minimum values.
2. How to create a simple Bank Account class with deposit, withdrawal, overdraft capabilities, and additional functionalities.
3. The importance of handling invalid input and maintaining a consistent account state.
4. How to use class methods to enable or disable features (e.g., overdraft) and provide a string representation of the class for better readability.

Further Reading:
For more information on loops and classes in Python, visit the [Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements) and [Python Classes](https://docs.python.org/3/tutorial/classes.html).
"""
