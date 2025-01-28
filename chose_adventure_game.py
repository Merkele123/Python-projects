import random

# Random events
cannibals_appear = random.randint(0, 1)
wild_animal = random.choice(["bear", "wolf", "tiger"])
storm = random.randint(0, 1)

# Get player's name
name = input("Type your name: ")
print(f"Welcome, {name}, to this epic adventure!\n")

# First decision: Left or Right
answer = input("You are trying to get back home through dangerous areas. "
               "You can choose which way to go, left or right: ").lower()

if answer == "left":
    # Second decision: Cannibal village
    answer = input("You come to a village of cannibals. Do you 'go through' the village "
                   "or 'go around' it? ").lower()
    
    if answer == "go through":
        if cannibals_appear == 1:
            print("The cannibals saw you and ate you. You lost!")
        else:
            print("You carefully walked through the village without being noticed. You survived this part!")
            
            # Third decision: Forest or River
            answer = input("Ahead of you is a dense forest and a wide river. "
                           "Do you go into the 'forest' or swim across the 'river'? ").lower()
            
            if answer == "forest":
                if wild_animal == "bear":
                    print("A bear attacked you in the forest. You couldn't escape. You lost!")
                else:
                    print(f"You encountered a {wild_animal}, but managed to scare it away. You survived!")
            elif answer == "river":
                if storm == 1:
                    print("A sudden storm hit while you were swimming. You couldn't make it. You lost!")
                else:
                    print("You swam across the river safely. You're getting closer to home!")
            else:
                print("Not a valid option. You got lost in the wilderness.")
    
    elif answer == "go around":
        print("You took the long way around and avoided the cannibals. Smart choice!")
        # Bonus survival decision
        answer = input("You find a cave to rest. Do you 'enter' the cave or 'keep walking'? ").lower()
        if answer == "enter":
            print("The cave was safe, and you regained your strength. You survived this part!")
        elif answer == "keep walking":
            print("You got too tired and collapsed. A passing traveler found and saved you!")
        else:
            print("Not a valid option. You hesitated and night fell, leaving you vulnerable.")
    else:
        print("Not a valid option. You hesitated too long and got lost.")
        
elif answer == "right":
    # Second decision: River or Bridgedi
    answer = input("You come to a raging river. Do you 'swim' across or 'wait' for a bridge to appear? ").lower()
    
    if answer == "swim":
        if storm == 1:
            print("A storm made the river too dangerous. You drowned. You lost!")
        else:
            print("You swam across the river safely. Good job!")
            # Third decision: Village or Mountains
            answer = input("You see a small village and towering mountains ahead. "
                           "Do you head to the 'village' or climb the 'mountains'? ").lower()
            
            if answer == "village":
                print("The villagers gave you food and directions. You are on the right track!")
            elif answer == "mountains":
                print("You climbed the mountains and found a beautiful view, but no way home.")
            else:
                print("Not a valid option. You wandered aimlessly and got lost.")
    
    elif answer == "wait":
        print("You waited patiently and a bridge magically appeared. You crossed safely!")
        # Bonus decision after crossing the bridge
        answer = input("On the other side, you find an old man offering help. "
                       "Do you 'trust' him or 'refuse' his help? ").lower()
        if answer == "trust":
            print("The old man guided you safely to the nearest town. You are almost home!")
        elif answer == "refuse":
            print("You went your own way but got lost in the wilderness. You lost!")
        else:
            print("Not a valid option. You missed your chance for help.")
    else:
        print("Not a valid option. You hesitated and were swept away by the river.")

else:
    print("Not a valid option. You stood still until nightfall, and something dangerous found you.")

print(f"Thank you for playing {name}!")
