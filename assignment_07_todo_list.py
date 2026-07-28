# Function to display the menu
def display_menu():
    print("\n============================")
    print("      TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


# Function to add a task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


# Function to view tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


# Function to delete a task
def delete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)

    task_number = int(input("Enter task number to delete: "))

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" has been removed.')
    else:
        print("Error: Invalid task number.")


# Main program
tasks = []

while True:
    display_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Error: Invalid choice. Please enter a number between 1 and 4.")