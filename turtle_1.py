import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "cyan",
    "magenta",
    "pink",
    "brown",
]


def get_num_of_tutrtles():
    racers = 0
    while True:
        racers = input("Enter the number of racers you wanna see (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric, please try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try again!!")

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
    
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            
def create_turtles(colors):
    turtles = []
    sapcingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * sapcingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing! 2")


racers = get_num_of_tutrtles()
turtles()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is turtle with color: {winner}")
time.sleep(5)