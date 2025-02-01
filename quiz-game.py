import time  # Importing the time module to track quiz duration
import random  # Importing the random module to shuffle and select random questions

# List of quiz questions with multiple-choice options
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A) Madrid", "B) Rome", "C) Paris", "D) Berlin"],
        "answer": "C"
    },
    {
        "prompt": "Who was the first President of the United States?",
        "options": ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson", "D) John Adams"],
        "answer": "B"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
        "answer": "C"
    },
    {
        "prompt": "In what year did World War II end?",
        "options": ["A) 1945", "B) 1939", "C) 1918", "D) 1950"],
        "answer": "A"
    },
    {
        "prompt": "What is the national currency of Japan?",
        "options": ["A) Yuan", "B) Yen", "C) Won", "D) Rupee"],
        "answer": "B"
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) Thailand", "D) South Korea"],
        "answer": "B"
    },
    {
        "prompt": "Which continent is the Sahara Desert located in?",
        "options": ["A) Asia", "B) Africa", "C) Australia", "D) South America"],
        "answer": "B"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
        "answer": "C"
    },
    {
        "prompt": "What is the smallest country in the world by land area?",
        "options": ["A) Monaco", "B) Vatican City", "C) San Marino", "D) Liechtenstein"],
        "answer": "B"
    }
]

def run_quiz(questions):
    """
    Function to conduct a timed multiple-choice quiz.

    Steps:
    - Selects a random subset of questions.
    - Asks each question and evaluates user answers.
    - Tracks time taken and total score.
    """

    score = 0  # Initialize the score counter
    start_time = time.time()  # Record the start time of the quiz

    # Select half of the questions randomly to make the quiz shorter
    selected_questions = random.sample(questions, len(questions) // 2)

    # Iterate through each selected question
    for question in selected_questions:
        print(question["prompt"])  # Print the question
        for option in question["options"]:  # Print all multiple-choice options
            print(option)

        # Get user input and convert to uppercase for case-insensitivity
        answer = input("Enter your answer (A, B, C, D): ").upper()

        # Check if the answer is correct
        if answer == question['answer']:
            print("Correct!!\n")
            score += 1  # Increase score if the answer is correct
        else:
            print(f"Wrong, you IDIOT!! The correct answer is {question['answer']}\n")

    end_time = time.time()  # Record the end time of the quiz
    total_time = round(end_time - start_time, 2)  # Calculate the total time taken

    # If the user takes too long, print a warning
    if total_time >= 15:
        print(f"You are too slow!! You finished it in: {total_time} seconds")
    else:
        print(f"Nice job!! You finished it in: {total_time} seconds")

    # Display the final score
    print(f"You got: {score} out of {len(questions) // 2} questions correct")
    
# Run the quiz with the list of questions
run_quiz(questions)
