import curses  # Library for terminal-based user interfaces
from curses import wrapper  # Wrapper for easy setup and teardown of curses
import time  # For time tracking
import random  # For selecting random lines from a text file


# Function to display the start screen
def start_screen(stdscr):
    stdscr.clear()  # Clear the screen
    stdscr.addstr("Welcome to the speed typing test!!")  # Display the welcome message
    stdscr.addstr("\nPress any key to begin")  # Prompt user to press any key to start
    stdscr.refresh()  # Refresh the screen to show text
    stdscr.getkey()  # Wait for the user to press a key


# Function to display target text, user input, and WPM
def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)  # Display the target text for typing
    stdscr.addstr(1, 0, f"WPM: {wpm}")  # Display the calculated Words Per Minute (WPM)

    # Loop to check the correctness of each character typed by the user
    for i, char in enumerate(current_text):
        correct_char = target_text[i]  # Corresponding correct character
        color = curses.color_pair(1)  # Default color (green) for correct characters
        if char != correct_char:  # If the character is incorrect
            color = curses.color_pair(2)  # Use the error color (red)
        stdscr.addstr(0, i, char, color)  # Display the character with the correct color


# Function to load a random line of text from the file
def load_text():
    with open("text.txt", "r") as f:  # Open the file containing text
        lines = f.readlines()  # Read all lines from the file
        return random.choice(lines).strip()  # Return a random line, stripped of whitespace


# Function to handle the actual typing test
def wpm_test(stdscr):
    target_text = load_text()  # Load the random text for the user to type
    current_text = []  # Store user input as a list of characters
    wpm = 0  # Initialize Words Per Minute counter
    start_time = time.time()  # Record the start time of the test
    stdscr.nodelay(True)  # Set the screen to non-blocking mode for real-time input

    while True:  # Infinite loop to handle typing until the user finishes or quits
        time_lapsed = max(time.time() - start_time, 1)  # Calculate elapsed time
        wpm = round((len(current_text) / (time_lapsed / 60)) / 5)  # WPM calculation formula
        stdscr.clear()  # Clear the screen for updating
        display_text(stdscr, target_text, current_text, wpm)  # Display current progress
        stdscr.refresh()  # Refresh the screen to show changes

        # Check if the user has completed typing the target text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  # Disable non-blocking mode
            break  # Exit the loop

        try:
            key = stdscr.getkey()  # Get a key press from the user
        except:
            continue  # Skip iteration if no key was pressed

        if ord(key) == 27:  # If "Esc" key is pressed, exit the loop
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):  # Handle backspace for deleting characters
            if len(current_text) > 0:
                current_text.pop()  # Remove the last character from user input
        elif len(current_text) < len(target_text):  # Ensure input length doesn't exceed target text
            current_text.append(key)  # Append the pressed key to the user's input


# Main function to initialize curses and control the flow of the program
def main(stdscr):
    # Initialize color pairs for curses
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green for correct text
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red for incorrect text
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default white text

    start_screen(stdscr)  # Display the welcome screen

    while True:  # Infinite loop to allow the user to retry or quit
        wpm_test(stdscr)  # Run the typing test
        stdscr.addstr(2, 0, "You completed the text, press any key to exit")  # Completion message
        key = stdscr.getkey()  # Wait for user input after the test
        if ord(key) == 27:  # If "Esc" key is pressed, exit the program
            break


# Wrapper function to handle curses initialization and cleanup
wrapper(main)
