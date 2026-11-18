"""Console interface for the Student Task Manager."""

from task_manager import TaskManager


def show_menu():
    print("\n===== Student Task Manager =====")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"Task added: {task}")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            manager.display_tasks()
            entry = input("Enter task ID to complete: ").strip()
            if not entry.isdigit():
                print("Error: Please enter a valid numeric task ID.")
            elif manager.complete_task(int(entry)):
                print("Task marked as completed.")
            else:
                print(f"Error: No task found with ID {entry}.")
        elif choice == "4":
            entry = input("Enter task ID to delete: ").strip()
            if not entry.isdigit():
                print("Error: Please enter a valid numeric task ID.")
            elif manager.delete_task(int(entry)):
                print("Task deleted.")
            else:
                print(f"Error: No task found with ID {entry}.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
