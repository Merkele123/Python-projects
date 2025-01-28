import random  # Import the random module for dice rolls

# Function to simulate a dice roll
def roll():
    min_value = 1  # Minimum value on the dice
    max_value = 6  # Maximum value on the dice
    roll = random.randint(min_value, max_value)  # Generate a random number between 1 and 6
    return roll  # Return the result of the roll

# Infinite loop to get a valid number of players
while True:
    players = input("Enter the number of players (2 - 4): ")  # Ask for the number of players
    if players.isdigit():  # Check if the input is a number
        players = int(players)  # Convert input to an integer
        if 2 <= players <= 4:  # Check if the number of players is between 2 and 4
            break  # Exit the loop if the conditions are met
        else:
            print("Must be between (2 - 4)")  # Notify the user of invalid input
    else:
        print("Invalid number of players, try again:")  # Notify the user of invalid input

max_score = 50  # Maximum score required to win the game
player_scores = [0 for _ in range(players)]  # List to store the scores of all players

# Main game loop
while max(player_scores) < max_score:  # Continue the game until someone reaches the max score
    for player_index in range(players):  # Loop through all players
        print(f"\nPlayer: {player_index + 1} turn has just started!\n")  # Notify the start of the player's turn
        print(f"Your total score is {player_scores[player_index]}")  # Display the player's current total score
        current_score = 0  # Initialize the current turn's score

        # Loop for rolling the dice during the player's turn
        while True:
            should_roll = input("Would you like to take a roll? Press 'y' ")  # Ask if the player wants to roll
            if should_roll.lower() != "y":  # If the player doesn't want to roll
                current_score = 0  # Reset the current turn's score to 0
                break  # Exit the rolling loop

            value = roll()  # Roll the dice
            if value == 1:  # If the roll result is 1
                print("You rolled a 1. Turn done")  # Notify that the turn is over
                break  # Exit the rolling loop
            else:
                current_score += value  # Add the roll result to the current turn's score
                print(f"You rolled a: {value}")  # Display the roll result
            print(f"Your current score is: {current_score}")  # Display the current turn's score

        # Add the current turn's score to the player's total score
        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")  # Display the player's total score

# After the game ends, determine the winner
max_score = max(player_scores)  # Find the highest score among all players
winning_idx = player_scores.index(max_score)  # Find the index of the player with the highest score
print(f"Player number {winning_idx + 1} is winning with the score of: {max_score}")  # Announce the winner


# def roll():
#     """Simulates rolling a die."""
#     return random.randint(1, 6)


# def get_player_count():
#     """Prompts the user to input a valid number of players."""
#     while True:
#         players = input("Enter the number of players (2-4): ")
#         if players.isdigit():
#             players = int(players)
#             if 2 <= players <= 4:
#                 return players
#             else:
#                 print("Number of players must be between 2 and 4.")
#         else:
#             print("Invalid input. Please enter a number between 2 and 4.")


# def take_turn(player_index, current_score):
#     """Handles a single player's turn."""
#     print(f"\nPlayer {player_index + 1}, it's your turn!")
#     print(f"Your current total score is {current_score}")
#     turn_score = 0

#     while True:
#         should_roll = input("Would you like to roll the die? (y to roll): ").strip().lower()
#         if should_roll != 'y':
#             print("You chose to end your turn.")
#             break

#         rolled_value = roll()
#         if rolled_value == 1:
#             print("You rolled a 1! Your turn is over, and you lose all turn points.")
#             turn_score = 0
#             break
#         else:
#             turn_score += rolled_value
#             print(f"You rolled a {rolled_value}.")
#             print(f"Your turn score is now {turn_score}.")

#     return turn_score


# def display_scores(player_scores):
#     """Displays the current scores of all players."""
#     print("\nCurrent Scores:")
#     for i, score in enumerate(player_scores):
#         print(f"Player {i + 1}: {score}")


# def play_game():
#     """Main function to play the dice game."""
#     max_score = 50
#     player_count = get_player_count()
#     player_scores = [0] * player_count

#     while max(player_scores) < max_score:
#         for player_index in range(player_count):
#             turn_score = take_turn(player_index, player_scores[player_index])
#             player_scores[player_index] += turn_score
#             print(f"Player {player_index + 1}'s total score is now {player_scores[player_index]}.")

#             if player_scores[player_index] >= max_score:
#                 break  # End game early if a player reaches the max score.

#         display_scores(player_scores)

#     # Determine the winner
#     winning_score = max(player_scores)
#     winning_player = player_scores.index(winning_score) + 1
#     print(f"\nCongratulations Player {winning_player}! You win with a score of {winning_score}.")


# if __name__ == "__main__":
#     play_game()
