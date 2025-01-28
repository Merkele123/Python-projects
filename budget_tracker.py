import json  # Importing the JSON module to handle saving and loading data

# Function to add an expense
def add_expenses(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})  # Add expense as a dictionary
    print(f"Added expense: {description}, Amount: {amount}\n")  # Confirm the addition

# Function to calculate the total of all expenses
def get_total_expenses(expenses):
    sum = 0  # Initialize total
    for expense in expenses:  # Loop through each expense
        sum += expense["amount"]  # Add the amount to the total
    return sum  # Return the total

# Function to calculate the remaining budget
def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)  # Subtract total expenses from the budget

# Function to display the current budget details
def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")  # Display the total budget
    print("Expenses:")  # Display all recorded expenses
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")  # Display each expense
    print(f"Total spent: {get_total_expenses(expenses)}")  # Show total expenses
    print(f"Remaining budget: {get_balance(budget, expenses)}\n")  # Show remaining budget

# Function to load budget and expenses data from a file
def load_budget_data(file_path):
    try:
        with open(file_path, "r") as file:  # Open the file in read mode
            data = json.load(file)  # Load the JSON data
            return data["initial_budget"], data["expenses"]  # Return budget and expenses
    except (FileNotFoundError, json.JSONDecodeError):  # Handle errors if the file doesn't exist or is invalid
        return 0, []  # Return default values

# Function to save budget and expenses data to a file
def save_budget_data(file_path, initial_budget, expenses):
    data = {"initial_budget": initial_budget, "expenses": expenses}  # Prepare data as a dictionary
    with open(file_path, "w") as file:  # Open the file in write mode
        json.dump(data, file, indent=4)  # Save data as JSON with indentation for readability

# Main function to control the app flow
def main():
    print("Welcome to the budget app!")  # Welcome message
    file_path = "budget_data.json"  # Define the file to store budget data
    initial_budget, expenses = load_budget_data(file_path)  # Load existing data
    if initial_budget == 0:  # If no budget is found, ask the user to enter a new budget
        initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget  # Assign the initial budget to the working budget

    while True:  # Infinite loop for the main menu
        print("What would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1 / 2 / 3): \n")  # Get the user's choice

        if choice == "1":  # Add an expense
            description = input("Enter expense description: ")  # Get description of the expense
            amount = float(input("Enter expense amount: "))  # Get the expense amount
            add_expenses(expenses, description, amount)  # Add the expense to the list
        elif choice == "2":  # Show budget details
            show_budget_details(budget, expenses)  # Display budget and expense details
        elif choice == "3":  # Exit the program
            save_budget_data(file_path, initial_budget, expenses)  # Save the data before exiting
            print("Exiting budget app")  # Exit message
            break  # Break out of the loop
        else:  # Handle invalid input
            print("Invalid choice, try again")

# Entry point of the script
if __name__ == "__main__":
    main()
