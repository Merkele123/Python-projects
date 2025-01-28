import json


def add_expenses(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}\n")


def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum


def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}\n")


def load_budget_data(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


def save_budget_data(file_path, initial_budget, expenses):
    data = {"initial_budget": initial_budget, "expenses": expenses}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def main():
    print("Welcome to the budget app!")
    file_path = "budget_data.json"
    initial_budget, expenses = load_budget_data(file_path)
    if initial_budget == 0:
        initial_budget = float(input("Please enter your inintial budget: "))
    budget = initial_budget

    while True:
        print("What would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choise = input("Enter your choise (1 / 2 / 3): \n")

        if choise == "1":
            description = input("Enter expense description: ")
            amount = float(input("Eneter expenses amount: "))
            add_expenses(expenses, description, amount)
        elif choise == "2":
            show_budget_details(budget, expenses)
        elif choise == "3":
            save_budget_data(file_path, initial_budget, expenses)
            print("Exiting budget app")
            break
        else:
            print("Invalid choise, try again")


if __name__ == "__main__":
    main()
