import random  # Importing the random module to generate the computer's choice

# Initialize scores
user_score = 0
pc_score = 0

# List of possible choices
options = ["rock", "paper", "scissors"]

# Start the game loop
while True:
    # Prompt user input and convert to lowercase
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    # If the user enters "Q" (to quit), exit the game loop
    if user_input == "q":
        break

    # Ensure the user enters a valid choice
    if user_input not in options:
        print("Invalid choice, please try again.")
        continue  # Restart the loop

    # Generate a random choice for the computer (0 = rock, 1 = paper, 2 = scissors)
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]  # Pick corresponding option
    print(f"Computer picked: {computer_pick}.")

    # Determine the winner
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!!")
        user_score += 1  # Increase user score
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!!")
        user_score += 1
    elif user_input == computer_pick:
        print("It's a draw.")  # If both choices are the same, it's a tie
    else:
        print("You lost!!!")
        pc_score += 1  # Increase computer's score

# Display final scores when the user quits
print(f"\nFinal Scores:\nYou won: {user_score} times.\nComputer won: {pc_score} times.")
print("Goodbye!")
