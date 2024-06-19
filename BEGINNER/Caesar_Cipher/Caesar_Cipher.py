#Caesar Cipher

import caesar_cipher_art

# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Function to perform Caesar encryption or decryption
def caesar(text, shift, direction):
    result_text = ""
    shift = shift % 26  # Ensure shift is within the range of the alphabet size

    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if direction == 'encode':
                new_char_index = (char_index + shift) % 26
            elif direction == 'decode':
                new_char_index = (char_index - shift) % 26
            result_text += alphabet[new_char_index]
        else:
            result_text += char

    return result_text

# Function to ask the user if they want to restart the program
def restart_program():
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    return restart == 'yes'

print(caesar_cipher_art.logo)  # Print the logo from caesar_cipher_art.py

#game
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number (e.g., 1-26):\n"))

    if direction == 'encode' or direction == 'decode':
        result_message = caesar(text, shift, direction)
        print(f"The {direction}d text is: {result_message}")
    else:
        print("Invalid input. Please enter 'encode' or 'decode' for direction.")

    if not restart_program():
        break
