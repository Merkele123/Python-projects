import random  # Importing the random module for generating random numbers
import time  # Importing the time module to measure how long the user takes to complete the problems

# List of operators that can be used in the problems
OPERATORS = ["+", "-", "*"]

# Minimum and maximum values for operands in the math problems
MIN_OPERAND = 3
MAX_OPERAND = 12

# Total number of problems the user needs to solve
TOTAL_PROBLEMS = 5


def generate_problem():
    """
    Generates a random math problem using two operands and an operator.
    Returns:
        expr (str): The math expression as a string (e.g., "4 + 5").
        answer (int): The correct answer to the math problem.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random number for the left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random number for the right operand
    operator = random.choice(OPERATORS)  # Randomly select an operator from the OPERATORS list

    expr = str(left) + " " + operator + " " + str(right)  # Create the math expression as a string
    answer = eval(expr)  # Evaluate the expression to get the correct answer
    return expr, answer  # Return the expression and the correct answer


wrong = 0  # Initialize a counter for wrong attempts

# Prompt the user to start the quiz
input("Press enter to start:")
print("------------")

start_time = time.time()  # Record the start time of the quiz

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a new math problem
    
    while True:  # Keep asking the user until they provide the correct answer
        guess = input("Problem # " + str(i + 1) + ": " + expr + " = ")  # Get user input for the answer
        if guess == str(answer):  # Check if the answer is correct
            break  # Exit the loop if the answer is correct
        wrong += 1  # Increment the wrong answer counter if the answer is incorrect

end_time = time.time()  # Record the end time of the quiz
total_time = round(end_time - start_time, 2)  # Calculate the total time taken to complete the quiz

print("------------")
print(f"Nice job! You finished it in: {total_time} seconds")  # Display the completion time
