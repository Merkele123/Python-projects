import random  # Importing random to shuffle and select random words for the quiz
import time  # Importing time to measure how long the user takes to complete the quiz

# List of words with their English and Estonian translations
words = [
    {"English": "house", "Estonian": "maja"},
    {"English": "car", "Estonian": "auto"},
    {"English": "book", "Estonian": "raamat"},
    {"English": "tree", "Estonian": "puu"},
    {"English": "water", "Estonian": "vesi"},
    {"English": "food", "Estonian": "toit"},
    {"English": "friend", "Estonian": "sõber"},
    {"English": "family", "Estonian": "perekond"},
    {"English": "dog", "Estonian": "koer"},
    {"English": "cat", "Estonian": "kass"},
    {"English": "city", "Estonian": "linn"},
    {"English": "country", "Estonian": "riik"},
    {"English": "school", "Estonian": "kool"},
    {"English": "teacher", "Estonian": "õpetaja"},
    {"English": "student", "Estonian": "õpilane"},
    {"English": "child", "Estonian": "laps"},
    {"English": "day", "Estonian": "päev"},
    {"English": "night", "Estonian": "öö"},
    {"English": "morning", "Estonian": "hommik"},
    {"English": "evening", "Estonian": "õhtu"},
    {"English": "love", "Estonian": "armastus"},
    {"English": "happiness", "Estonian": "õnn"},
    {"English": "sun", "Estonian": "päike"},
    {"English": "moon", "Estonian": "kuu"},
    {"English": "star", "Estonian": "täht"},
    {"English": "river", "Estonian": "jõgi"},
    {"English": "mountain", "Estonian": "mägi"},
    {"English": "sea", "Estonian": "meri"},
    {"English": "lake", "Estonian": "järv"},
    {"English": "forest", "Estonian": "mets"},
    {"English": "flower", "Estonian": "lill"},
    {"English": "bird", "Estonian": "lind"},
    {"English": "fish", "Estonian": "kala"},
    {"English": "rain", "Estonian": "vihm"},
    {"English": "snow", "Estonian": "lumi"},
    {"English": "wind", "Estonian": "tuul"},
    {"English": "fire", "Estonian": "tuli"},
    {"English": "earth", "Estonian": "maa"},
    {"English": "sky", "Estonian": "taevas"},
    {"English": "road", "Estonian": "tee"},
    {"English": "bridge", "Estonian": "sild"},
    {"English": "chair", "Estonian": "tool"},
    {"English": "table", "Estonian": "laud"},
    {"English": "bed", "Estonian": "voodi"},
    {"English": "window", "Estonian": "aken"},
    {"English": "door", "Estonian": "uks"},
    {"English": "kitchen", "Estonian": "köök"},
    {"English": "bathroom", "Estonian": "vannituba"},
    {"English": "garden", "Estonian": "aed"},
    {"English": "shop", "Estonian": "pood"},
    {"English": "market", "Estonian": "turg"},
    {"English": "money", "Estonian": "raha"},
    {"English": "bank", "Estonian": "pank"},
    {"English": "computer", "Estonian": "arvuti"},
    {"English": "phone", "Estonian": "telefon"},
    {"English": "television", "Estonian": "televisioon"},
    {"English": "radio", "Estonian": "raadio"},
    {"English": "music", "Estonian": "muusika"},
    {"English": "song", "Estonian": "laul"},
    {"English": "dance", "Estonian": "tants"},
    {"English": "movie", "Estonian": "film"},
    {"English": "game", "Estonian": "mäng"},
    {"English": "sport", "Estonian": "sport"},
    {"English": "health", "Estonian": "tervis"},
    {"English": "medicine", "Estonian": "ravim"},
    {"English": "hospital", "Estonian": "haigla"},
    {"English": "doctor", "Estonian": "arst"},
    {"English": "nurse", "Estonian": "õde"},
    {"English": "police", "Estonian": "politsei"},
    {"English": "firefighter", "Estonian": "tulekustutaja"},
    {"English": "post", "Estonian": "post"},
    {"English": "letter", "Estonian": "kiri"},
    {"English": "bookstore", "Estonian": "raamatupood"},
    {"English": "library", "Estonian": "raamatukogu"},
    {"English": "office", "Estonian": "kontor"},
    {"English": "work", "Estonian": "töö"},
    {"English": "job", "Estonian": "amet"},
    {"English": "holiday", "Estonian": "puhkus"},
    {"English": "vacation", "Estonian": "puhkus"},
    {"English": "travel", "Estonian": "reisimine"},
    {"English": "train", "Estonian": "rong"},
    {"English": "bus", "Estonian": "buss"},
    {"English": "plane", "Estonian": "lennuk"},
    {"English": "ship", "Estonian": "laev"},
    {"English": "bicycle", "Estonian": "jalgratas"},
    {"English": "schoolbag", "Estonian": "koolikott"},
    {"English": "notebook", "Estonian": "märkmik"},
    {"English": "pen", "Estonian": "pastakas"},
    {"English": "pencil", "Estonian": "pliiats"},
    {"English": "eraser", "Estonian": "kustutuskumm"},
    {"English": "clock", "Estonian": "kell"},
    {"English": "watch", "Estonian": "käekell"},
    {"English": "calendar", "Estonian": "kalender"},
]



def quiz_user(words):
    """
    Function to quiz the user with random Estonian words
    and ask for their English translations.
    """
    selected_words = random.sample(words, 5)  # Select 5 random words for the quiz
    score = 0  # Initialize the user's score to zero
    
    for word in selected_words:  # Loop through each randomly selected word
        time_start = time.time()  # Start the timer for the quiz
        print(f"What is the English translation of '{word['Estonian']}'?")  # Show the Estonian word
        user_answer = input("Your answer: ").strip().lower()  # Get user's answer and normalize it to lowercase
        correct_answer = word["English"].lower()  # Normalize the correct answer to lowercase for comparison

        if user_answer == correct_answer:  # Check if the user's answer is correct
            print("Correct\n")
            score += 1  # Increment the score for a correct answer
        else:
            # Inform the user of the correct answer if they were wrong
            print(f"Wrong, you idiot! The correct answer is {word['English']}\n")

    end_time = time.time()  # Stop the timer when the quiz is over
    total_time = round(end_time - time_start, 2)  # Calculate total time taken and round to 2 decimal places

    # Display the user's final score and time taken
    print(f"Quiz is over!! Your score is: {score} / {len(selected_words)}")
    print(f"It took you: {total_time} seconds")


def main():
    """
    Main function to welcome the user and start the quiz.
    """
    print("Welcome to the language learning app")  # Welcome message
    input("Press ENTER to start the program...")  # Wait for the user to press Enter before starting
    quiz_user(words)  # Call the quiz_user function to start the quiz


# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the app
