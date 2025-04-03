"""
todo.py is a simple to-do list application that
keeps a user's to-do list as a text file.

Users can add, list or remove tasks.
"""
import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Add a new task to the list."""
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")

def list_tasks():
    """Return a string representation of all tasks."""
    output_string = ""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                output_string += f"{index}. {task.strip()}\n"
    return output_string  # Do not strip, keep trailing newline

def remove_task(index):
    """Remove a task by its 1-based index."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        if index < 1 or index > len(tasks):
            print("Invalid index.")
            return
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed.")
    else:
        print("No tasks found.")

def main():
    """Parse command-line arguments and execute the corresponding action."""
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        try:
            index = int(args.remove)
            remove_task(index)
        except ValueError:
            print("Please provide a valid integer index.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()