#import - keyword (להוסיף ספרייה לקוד שלנו)
# import random (ייבא לקוד שלי את כל ספריית ראנדום)

# pip install {שם הספריה} (אם לא נמצאה הספרייה אפשר להתקין אותה עם השורת פקודה הבאה בטרמינל) 
from random import randint

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


def dice_builder(n):
    #posible
    top =    " _______ "
    botton = "|_______|"
    empty =  "|       |"
    mid =    "|   o   |"
    two =    "| o   o |" 
    left =   "| o     |"
    right =  "|     o |"     

    dice = ""

    dice += top + "\n" + empty + "\n"
    match n:
        case 1:
            dice += empty + "\n" + mid + "\n" + empty + "\n"
        case 2:    
            dice += left + "\n" + empty + "\n" + right + "\n"
        case 3:
            dice += left + "\n" + mid + "\n" + right + "\n"
        case 4:
            dice += two + "\n" + empty + "\n" + two + "\n"
        case 5:
            dice += two + "\n" + mid + "\n" + two + "\n"
        case 6:
            dice += two + "\n" + two + "\n" + two + "\n"

    dice += botton

    return dice



# print(*dice2, sep='\n')
# print(*dice3, sep='\n')

dice_list = []
for i in range(1, 7):
    dice_list.append(dice_builder(i).split("\n"))

# print(dice_list)


def merge_list(dice_list):
    number_of_dice = len(dice_list)
    dice_size = len(dice_list[0])
    merge_list = []
    for i in range(dice_size):
        for j in range(number_of_dice):
            merge_list.append(dice_list[j][i])

    return merge_list

def print_ndice(dice_list, number):
    for i in range(len(dice_list)):
        print(dice_list[i], end='\t')
        if i % number == 1 and i != 0:
            print()
        

def main():
    commend = ""
    while True:

        # get user input
        commend = input("enter a number of dice you would like to roll or quit to exit: ")


        # exit condition
        if commend.lower() == "quit":
            print("thanks for playing")
            break
        
        # allowed non-digit first chars
        prefix = ["-","+"]

        # check if the user entered a number
        if commend.isdigit() or (commend[1:].isdigit() and commend[0] in prefix):
            number_of_rolls = abs(int(commend))
        else:
            number_of_rolls = 1

        # roll given number of dice
        dice_list = []    
        for i in range(number_of_rolls):    
            dice = dice_builder(randint(1,6))
            dice_list.append(dice)

        print_ndice(merge_list(dice_list), len(dice_list))

main()