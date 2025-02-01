import turtle  # Importing the turtle module for graphics
import time  # Importing the time module for delays
import random  # Importing the random module for movement randomness

# Constants for screen width and height
WIDTH, HEIGHT = 500, 500

# List of available colors for the turtles
COLORS = [
    "red", "green", "blue", "yellow", "orange",
    "purple", "cyan", "magenta", "pink", "brown"
]


def get_num_of_turtles():
    """
    Prompts the user to enter the number of turtles (racers) for the race.
    Ensures the input is a valid number between 2 and 10.
    Returns:
        int: Number of racers.
    """
    while True:
        racers = input("Enter the number of racers you want (2 - 10): ")
        if racers.isdigit():  # Check if input is numeric
            racers = int(racers)
        else:
            print("Input is not numeric, please try again!")
            continue  # Restart input prompt if invalid

        if 2 <= racers <= 10:  # Ensure number is within valid range
            return racers
        else:
            print("Number not in range 2 - 10. Try again!!")


def race(colors):
    """
    Simulates the turtle race.
    Moves each turtle forward randomly until one reaches the finish line.

    Args:
        colors (list): List of turtle colors participating in the race.

    Returns:
        str: The winning turtle's color.
    """
    turtles = create_turtles(colors)  # Create turtles on the track

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # Random distance for movement
            racer.forward(distance)  # Move turtle forward

            # Get current turtle position
            x, y = racer.pos()

            # Check if turtle crossed the finish line (upper screen border)
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]  # Return winner's color


def create_turtles(colors):
    """
    Creates and positions the turtle racers at the starting line.

    Args:
        colors (list): List of turtle colors.

    Returns:
        list: List of turtle objects.
    """
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)  # Equal spacing for turtle start positions

    for i, color in enumerate(colors):
        racer = turtle.Turtle()  # Create turtle object
        racer.color(color)  # Set turtle color
        racer.shape("turtle")  # Set turtle shape
        racer.left(90)  # Face turtle upwards (towards finish line)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)  # Position turtles
        racer.pendown()
        turtles.append(racer)  # Add turtle to list

    return turtles


def setup_screen():
    """
    Sets up the turtle race screen with a title and dimensions.
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # Set screen size
    screen.title("Turtle Racing!")  # Set window title


# Get user input for number of racers
racers = get_num_of_turtles()

# Set up the race screen
setup_screen()

# Shuffle colors and select the required number for the race
random.shuffle(COLORS)
colors = COLORS[:racers]

# Start the race and determine the winner
winner = race(colors)
print(f"The winner is the turtle with color: {winner}")

# Delay before closing the program so user can see the result
time.sleep(5)
