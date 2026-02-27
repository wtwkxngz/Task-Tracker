tasks = []


def newOperation(all_tasks):
    while True:
        operation = input("Press 'a' to add a task, 'r' to remove a task, 'e' to edit a task, or 'q' to quit: ")
        if operation == 'a':
            addTask(all_tasks)
        elif operation == 'e':
            editTask(all_tasks)
        elif operation == 'r':
            removeTask(all_tasks)
        elif operation == 'q':
            print("Goodbye!")
            return
        else:
            print("Invalid operation. Please try again.")
        displayTasks(all_tasks)


def addTask(all_tasks):
    new_task = input("Add a new task: ")
    all_tasks.append(new_task)
    print(f"Task '{new_task}' added successfully!")


def editTask(all_tasks):
    displayTasks(all_tasks)
    if not all_tasks:
        print("No tasks to edit.")
        return
    try:
        index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= index < len(all_tasks):
            new_task = input("Enter the new task description: ")
            old_task = all_tasks[index]
            all_tasks[index] = new_task
            print(f"Task '{old_task}' updated to '{new_task}' successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def removeTask(all_tasks):
    displayTasks(all_tasks)
    if not all_tasks:
        print("No tasks to remove.")
        return
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(all_tasks):
            removed = all_tasks.pop(index)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Auxiliary functions
def displayTasks(all_tasks):
    print("Current tasks:")
    if not all_tasks:
        print("  (no tasks)")
        return
    for index, task in enumerate(all_tasks):
        print(f"{index + 1}. {task}")


# Start application
newOperation(tasks)
