def user_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks():
    try:
        with open("tasks.txt", "r") as files:
            task = files.readlines()
            if not task:
                print("No task found")
            else:
                print("\n --Your Tasks--")
                for i, task in enumerate(task, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("File not found")


def add_task():
    task = input("Enter a task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")


def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to complete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
                print("Task compleated and removed!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks file found.")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to complete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
                print("Task deleted successfully!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("No tasks file found.")


def Main():
    while True:
        user_menu()
        user = input("Hello, choose an option\n")
        if user == "1":
            view_tasks()
        elif user == "2":
            add_task()
        elif user == "3":
            complete_task()
        elif user == "4":
            delete_task()
        elif user == "5":
            print("Exiting the application. Goodbye!  ")
            break
        else:
            print("Invalid choice, please try again.")


Main()
