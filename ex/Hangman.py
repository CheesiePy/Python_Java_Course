import random

# List of words for the game
words = ["python", "programming", "language", "computer", "science"]

# Randomly select a word from the list
word = random.choice(words)

# Initialize variables
guessed_letters = []
lives = 6

# Main game loop
while lives > 0:
    # Display the word with unguessed letters replaced by underscores
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # Get input from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    # Check if the letter is in the word
    elif guess in word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        print("Incorrect.")
        lives -= 1

        
    print("You have {} lives remaining.".format(lives))
    if "_" not in display:
        print("You win!")
        break
        
# Handle the case when user loses
if lives == 0:
    print("You lose! The word was {}".format(word))