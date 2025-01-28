import random

user_score = 0
pc_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "Q".lower():
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!!")
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!!")
        user_score += 1
    elif user_input == computer_pick:
        print("It's a draw")
    else:
        print("Ypu lost!!!")
        pc_score += 1

print(f"You won: {user_score} time.\n The computer wins {pc_score} times.")
print("Goodbye!")
