from playsound import playsound  # Library to play sound files
import time  # Library for time-related functions

# ANSI escape codes for clearing the terminal and resetting the cursor
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(sec):
    """Counts down from the given number of seconds and plays an alarm sound."""
    time_elapsed = 0  # Track elapsed time

    print(CLEAR)  # Clear the terminal screen
    while time_elapsed < sec:
        time.sleep(1)  # Pause for 1 second
        time_elapsed += 1  # Increment elapsed time

        # Calculate remaining time in minutes and seconds
        time_left = sec - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Display the countdown timer in MM:SS format
        print(f"{CLEAR_AND_RETURN}Alarm will start in: {minutes_left:02d}:{seconds_left:02d}")

    # Play the alarm sound when the countdown finishes
    playsound("alarm.mp3")


# Input from the user
minutes = int(input("How many minutes to wait: "))  # Get minutes
seconds = int(input("How many seconds to wait: "))  # Get seconds

# Calculate total seconds for the countdown
total_seconds = minutes * 60 + seconds

# Start the alarm
alarm(total_seconds)
