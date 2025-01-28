from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(sec):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < sec:
        time.sleep(1)
        time_elapsed += 1

        time_left = sec - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will start in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")
    
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_secconds = minutes * 60 + seconds

alarm(total_secconds)