"""TASK TO DO LIST APPLICATION """
import os
import argparse

TASK_FILE = os.path.join(os.path.dirname(__file__), "test", "test_list.txt")


def add_task(task):
    """Function: add_task

    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")
        return

def list_tasks():
    """Read and return all tasks as a numbered list."""
    if not os.path.exists(TASK_FILE):
        return ""

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
        return "\n".join(f"{i + 1}. {line}" for i, line in enumerate(lines))


def remove_task(index):
    """Function: remove_task

    Input - a task to add to the list
    Return - nothing
    """

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed.")
    else:
        print("No tasks found.")

def main():
    """ SOMETHING """
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
