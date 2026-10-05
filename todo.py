tasks = []


def show_tasks():
    if not tasks:
        print("\nYour To-Do List is empty.")
        return

    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['name']}")


def add_task():
    task_name = input("\nEnter a task: ").strip()

    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter the task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted: {removed_task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== Python To-Do List =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
