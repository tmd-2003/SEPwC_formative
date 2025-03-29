import os
import argparse

task_file = os.path.join(os.path.dirname(__file__), "test", "test_list.txt")


def add_task(task):
    """Function: add_task

    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
       file.write(task + "\n")
       
       return 
      

def list_tasks():
  
    with open(task_file, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        counter = 1
        output_string = ""
        for task in tasks:
            output_string += f"{counter}. {task}"
            counter += 1

    return output_string.rstrip()


def remove_task(index):
    return

def main():
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
