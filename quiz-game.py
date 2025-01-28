import time
import random

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
    score = 0
    start_time = time.time()
    selected_questions = random.sample(questions, len(questions) // 2)
    
    for question in selected_questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question['answer']:
            print("Correct!!\n")
            score += 1
        else:
            print(f"Wrong, you IDIOT!! The correct answer is {question['answer']}\n")
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    if total_time >= 15:
        print(f"You are to slow!! You finished it in: {total_time} seconds")
    else:
        print(f"Nice job!! You finished it in: {total_time} seconds") 
    print(f"You got: {score} out of {len(questions) // 2} questions correct")
    
run_quiz(questions)



# def run_quiz(questions):
#     # Use `random.sample` to select half the questions randomly.
#     selected_questions = random.sample(questions, len(questions) // 2)

#     # Use a generator to iterate over the selected questions and calculate the score:
#     score = sum(
#         1 if (answer := input(
#             f"{q['prompt']}\n" + "\n".join(q['options']) + "\nEnter your answer (A, B, C, D): ").upper()) == q['answer']
#         else print(f"Wrong, you IDIOT!! The correct answer is {q['answer']}\n") or 0
#         for q in selected_questions
#     )
#     # After the quiz ends, print the final score and time taken:
#     print(f"\nYou got: {score} out of {len(selected_questions)} questions correct")  # Print the number of correct answers.
#     print(f"Nice job! You finished it in: {round(time.time() - start_time, 2)} seconds")  # Print time elapsed.

# # Start the timer before running the quiz.
# start_time = time.time()  # Record the starting time.
# run_quiz(questions)  # Call the `run_quiz` function with the list of questions.

