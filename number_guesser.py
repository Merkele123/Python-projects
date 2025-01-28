import random  # Import the random module for generating random numbers

# Ask the user to input the upper limit for the guessing range
top_of_range = input("Type a number: ")

# Check if the input is a valid number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Convert the input to an integer

    # Ensure the entered number is greater than 0
    if top_of_range <= 0:
        print("Please enter a number greater than 0")  # Notify the user if the number is invalid
        quit()  # Exit the program
else:
    # If the input is not a digit, prompt the user and quit the program
    print("Please enter a number greater than 0")
    quit()

# Generate a random number between 0 and the upper limit specified by the user
random_number = random.randint(0, top_of_range)
guesses = 0  # Initialize the guess counter

# Start the guessing loop
while True:
    guesses += 1  # Increment the guess counter
    user_guess = input("Make a guess: ")  # Prompt the user to make a guess

    # Check if the user's input is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)  # Convert the input to an integer
    else:
        # Notify the user if the input is invalid and prompt again
        print("Please enter a number next time")
        continue  # Restart the loop

    # Check if the user's guess matches the random number
    if user_guess == random_number:
        print(f"Correct!! You guessed: {guesses} times")  # Notify the user of success and the number of guesses
        break  # Exit the loop as the correct guess has been made
    elif user_guess > random_number:
        # Inform the user if their guess is too high
        print("You were above the number")
    else:
        # Inform the user if their guess is too low
        print("You were below the number!!")
