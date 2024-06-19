#Hangman

import random
from hangman_data import word_list  # Import the word list from hangman_data.py
from hangman_art import logo, stages    # Import the game logo and stages from hangman_art.py

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False  # Initialize a flag to track if the game has ended
lives = 6            # Initialize the number of lives

# Print the game logo
print(logo)

# For testing purposes, reveal the chosen word (remove in production)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []  # Create a list to track guessed letters

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # Ask the user for a guess and convert it to lowercase

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'.")  # Check if the letter has already been guessed
        continue  # Skip the rest of the loop and let the user guess again

    guessed_letters.append(guess)  # Add the guessed letter to the list

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # Check if the guess is correct and update the display

    if guess not in chosen_word:
        lives -= 1  # Reduce lives if the guess is incorrect
        if lives == 0:
            end_of_game = True  # Check if the user has run out of lives and end the game
            print("You lose.")

    print(f"{' '.join(display)}")  # Display the current state of the word with guessed letters

    if "_" not in display:
        end_of_game = True  # Check if the user has guessed all the letters and won
        print("You win.")

    print(stages[lives])  # Display the hangman stage based on the number of lives remaining
