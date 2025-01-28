import random

# List of possible words for the game
words = ["apple", "window", "forest", "pencil", "journey", "coffee", "island", "garden", "rainbow", "mountain"]

# Choose a random word from the list
chosen_word = random.choice(words)

# Create a list that will display underscores for each letter in the chosen word
word_display = ['_' for _ in chosen_word]

# Number of attempts
attempts = 8

print("Welcome to Hangman!")  # Welcome message

# While the player has attempts remaining and there are underscores in the word
while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))  # Display the current state of the word
    guess = input("Guess a letter: ").lower()  # Request a letter input and convert to lowercase
    
    # Check if the guessed letter is in the word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the guessed letter
    else:
        attempts -= 1  # Decrease the number of attempts
        print(f"That's a wrong letter! Try again! You have {attempts} attempts left.")

# After the loop ends, check if the word was guessed
if '_' not in word_display:
    print("You guessed the word!") 
    print(' '.join(word_display))  # Display the fully guessed word
    print("You survived!")
else:
    print(f"You ran out of attempts. The word was: {chosen_word}")  # Inform the player they lost
    print("You died!")
