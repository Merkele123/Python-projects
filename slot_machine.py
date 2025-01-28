import random  # Import the random module to generate random outcomes

# Constants to define the game settings
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Defining how many times each symbol appears in the machine
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

# Values for each symbol (how much they pay out)
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

# Function to check if a line is a winning line
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize the winnings
    winning_lines = []  # Initialize the list to store winning lines
    for line in range(lines):  # Iterate through each line
        symbol = columns[0][line]  # Get the symbol from the first column of the line
        for column in columns:  # Check if all columns have the same symbol for this line
            if column[line] != symbol:  # If the symbols don't match, it's not a winning line
                break
        else:  # If all symbols match, it's a winning line
            winnings += values[symbol] * bet  # Add the winnings for this line
            winning_lines.append(line + 1)  # Add the winning line number (starting from 1)
    return winnings, winning_lines  # Return the total winnings and the list of winning lines

# Function to simulate a spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # Create an empty list to hold all the symbols
    for symbol, symbol_count in symbols.items():  # For each symbol and its count
        for _ in range(symbol_count):  # Add the symbol to the list based on its count
            all_symbols.append(symbol)
    columns = []  # List to hold the columns of the slot machine
    for _ in range(cols):  # For each column in the machine
        column = []  # Create an empty column
        current_symbols = all_symbols[:]  # Copy the list of all symbols to avoid mutation issues
        for _ in range(rows):  # For each row in the column
            value = random.choice(current_symbols)  # Randomly select a symbol
            current_symbols.remove(value)  # Remove the selected symbol to avoid repetition
            column.append(value)  # Add the symbol to the column
        columns.append(column)  # Add the column to the list of columns
    return columns  # Return the generated slot machine columns

# Function to print the slot machine grid
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Iterate through each row
        for i, column in enumerate(columns):  # For each column
            if i != len(columns) - 1:  # If it's not the last column
                print(column[row], "|", end=" | ")  # Print the symbol and separator
            else:
                print(column[row], "|", end="")  # Print the last symbol without extra separator
        print()  # Move to the next row

# Function to prompt the user to deposit an amount
def deposit():
    while True:
        amount = input("What would you like to deposit? €")  # Ask user for deposit amount
        if amount.isdigit():  # Check if the input is a number
            amount = int(amount)  # Convert the input to an integer
            if amount > 0:  # Ensure the amount is greater than 0
                break
            else:
                print("Amount should be greater than 0.")  # Error message for invalid amount
        else:
            print("Please enter a number!")  # Error message for non-numeric input
    return amount  # Return the deposited amount

# Function to get the number of lines the player wants to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")  # Ask the user for line input
        if lines.isdigit():  # Check if the input is a number
            lines = int(lines)  # Convert the input to an integer
            if 1 <= lines <= MAX_LINES:  # Ensure the number of lines is within the valid range
                break
            else:
                print("Enter a valid number of lines.")  # Error message for invalid number of lines
        else:
            print("Please enter a number of lines!")  # Error message for non-numeric input
    return lines  # Return the number of lines the player wants to bet on

# Function to prompt the user for the bet amount per line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? €")  # Ask user for bet amount
        if amount.isdigit():  # Check if the input is a number
            amount = int(amount)  # Convert the input to an integer
            if MIN_BET <= amount <= MAX_BET:  # Ensure the bet is within the allowed range
                break
            else:
                print(f"Amount should be between €{MIN_BET} - €{MAX_BET}.")  # Error message for invalid bet amount
        else:
            print("Please enter a number!")  # Error message for non-numeric input
    return amount  # Return the bet amount

# Function to simulate a spin and handle the game logic
def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines to bet on
    while True:
        bet = get_bet()  # Get the bet amount per line
        total_bet = bet * lines  # Calculate the total bet based on the number of lines

        if total_bet > balance:  # Check if the user has enough balance
            print(
                f"You don't have enough to bet that amount, your current balance is {balance}€."
            )
        else:
            break  # Exit the loop if the bet is valid

    print(
        f"You are betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}"
    )

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Get the slot machine spin result
    print_slot_machine(slots)  # Print the slot machine grid
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check for winnings
    print(f"You won €{winnings}.")  # Print the winnings
    print(f"You won on lines: ", *winning_lines)  # Print the winning lines
    return winnings - total_bet  # Return the net winnings (winnings - bet)

# Main function to run the game
def main():
    balance = deposit()  # Get the initial deposit
    while True:
        print(f"Current balance is €{balance}.")  # Display the current balance
        answer = input("Press enter to play (q to quit): ")  # Prompt the user to start or quit
        if answer.lower() == "q":  # If the user enters 'q', exit the game
            break
        balance += spin(balance)  # Call the spin function and update the balance based on the winnings
        print(f"You left with €{balance}")  # Display the remaining balance after the spin

# Run the main function to start the game
main()
