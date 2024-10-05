"""
Lesson 8: Dice Simulation and Importing Modules

In this lesson, we will learn how to import libraries, create dice using ASCII art, and merge multiple dice representations for printing.
"""

# Importing necessary modules
from random import randint

# Dictionary for dice representation using ASCII art
dice_dict = {
    1:"""
     _______
    |       |
    |       |
    |   o   |
    |       |
    |_______|""",
    2:"""
     _______
    |       |
    | o     |
    |       |
    |     o |
    |_______|""",
    3:"""
     _______
    |       |
    | o     |
    |   o   |
    |     o |
    |_______|""",
    4:"""
     _______
    |       |
    | o   o |
    |       |
    | o   o |
    |_______|""",
    5:"""
     _______
    |       |
    | o   o |
    |   o   |
    | o   o |
    |_______|""",
    6:"""
     _______
    |       |
    | o   o |
    | o   o |
    | o   o |
    |_______|"""
}

# Function to create dice using ASCII representation
def dice_builder(n):
    # Defining different parts of the dice
    top =    " _______ "
    bottom = "|_______|"
    empty =  "|       |"
    mid =    "|   o   |"
    two =    "| o   o |"
    left =   "| o     |"
    right =  "|     o |"     

    dice = ""

    # Building the dice based on the number
    dice += top + "\n" + empty + "\n"
    if n == 1:
        dice += empty + "\n" + mid + "\n" + empty + "\n"  # For 1, middle dot
    elif n == 2:    
        dice += left + "\n" + empty + "\n" + right + "\n"  # For 2, dots on left and right
    elif n == 3:
        dice += left + "\n" + mid + "\n" + right + "\n"  # For 3, dots on left, middle, and right
    elif n == 4:
        dice += two + "\n" + empty + "\n" + two + "\n"  # For 4, two dots on top and bottom
    elif n == 5:
        dice += two + "\n" + mid + "\n" + two + "\n"  # For 5, two dots on top and bottom, one in the middle
    elif n == 6:
        dice += two + "\n" + two + "\n" + two + "\n"  # For 6, two dots on top, middle, and bottom

    dice += bottom  # Add the bottom part of the dice

    return dice

# Function to merge multiple dice ASCII representations
def merge_list(dice_list):
    number_of_dice = len(dice_list)  # Number of dice to be merged
    dice_size = len(dice_list[0].split("\n"))  # Number of lines in each dice representation
    merged_list = []
    
    # Loop through each line of the dice
    for i in range(dice_size):
        merged_row = "\t".join(dice.split("\n")[i] for dice in dice_list)  # Join the corresponding lines of each dice with tabs
        merged_list.append(merged_row)  # Append the merged line to the merged list

    return merged_list

# Function to print multiple dice in a grid-like format
def print_ndice(dice_list):
    for row in dice_list:  # Loop through each row of the merged list
        print(row)  # Print the merged row
        
# Main function to handle user input and simulate dice rolls
def main():
    command = ""
    while True:
        # Get user input
        command = input("Enter a number of dice you would like to roll or 'quit' to exit: ")

        # Exit condition
        if command.lower() == "quit":
            print("Thanks for playing!")
            break
        
        # Allowed non-digit first characters
        prefix = ["-", "+"]

        # Check if the user entered a number
        if command.isdigit() or (command[1:].isdigit() and command[0] in prefix):
            number_of_rolls = abs(int(command))  # Convert the input to a positive integer
        else:
            number_of_rolls = 1  # Default to rolling one dice if input is invalid

        # Roll the given number of dice
        dice_list = []    
        for i in range(number_of_rolls):    
            dice = dice_builder(randint(1, 6))  # Generate a random dice face (1-6)
            dice_list.append(dice)  # Add the dice representation to the list

        # Print all the dice rolled
        print_ndice(merge_list(dice_list))  # Merge and print the dice representations

# Run the main function
main()

"""
In this lesson, you learned:
1. How to import libraries in Python using `import` and `from ... import`.
2. How to create ASCII art representations of dice.
3. How to simulate rolling multiple dice and print them in a grid format.
4. The importance of user input validation and handling different cases.

Further Reading:
For more information about importing modules and libraries, visit the [Python Docs on Importing](https://docs.python.org/3/reference/import.html).
"""