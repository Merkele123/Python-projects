# To-Do List Application

def user_menu():
    """
    Displays the menu options for the To-Do List application.
    """
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks():
    """
    Reads and displays the list of tasks from 'tasks.txt'.
    If no tasks are found, an appropriate message is displayed.
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\n-- Your Tasks --")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found. Add a task to create one.")


def add_task():
    """
    Allows the user to add a new task to the 'tasks.txt' file.
    """
    task = input("Enter a task: ").strip()
    if task:
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def complete_task():
    """
    Marks a task as completed by removing it from 'tasks.txt'.
    """
    view_tasks()  # Show current tasks before selection
    try:
        task_num = int(input("Enter the number of the task to complete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_num <= len(tasks):  # Check if task number is valid
            del tasks[task_num - 1]  # Remove the selected task
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task completed and removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No task file found. Add a task first.")


def delete_task():
    """
    Deletes a task from 'tasks.txt' based on user input.
    """
    view_tasks()  # Show current tasks before selection
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_num <= len(tasks):  # Check if task number is valid
            del tasks[task_num - 1]  # Remove the selected task
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No task file found. Add a task first.")


def main():
    """
    Main function that runs the To-Do List application in a loop.
    """
    while True:
        user_menu()  # Display menu options
        user_choice = input("Choose an option: ").strip()

        if user_choice == "1":
            view_tasks()
        elif user_choice == "2":
            add_task()
        elif user_choice == "3":
            complete_task()
        elif user_choice == "4":
            delete_task()
        elif user_choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the application
if __name__ == "__main__":
    main()
