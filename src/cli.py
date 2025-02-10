import argparse
from src.commands import add_task_command, list_task_command, update_task_command, delete_task_command,  reset_task_command

def setup_parser():
    parser = argparse.ArgumentParser(
        prog="Task Manager CLI", 
        description="A task manager to track your tasks and give valuable feedback")
    subparser = parser.add_subparsers(dest="command", required=True)
    
    #add command
    add_parser = subparser.add_parser("add", help="add task to the tracker")
    add_parser.add_argument("task", type=str, help="Task Description")
    add_parser.add_argument("--status", type=str, 
                            choices=["in-progress", "todo", "done"],
                            default="todo", help="Current status of task")
    add_parser.set_defaults(func=add_task_command)
    
    #list command
    add_parser = subparser.add_parser("list", help="lists current tasks")
    add_parser.add_argument("--status", type=str, 
                            choices=["in-progress", "todo", "done"],
                            help="Current status of task")
    add_parser.set_defaults(func=list_task_command)

    #update command
    add_parser = subparser.add_parser("update", help="update an existing task")
    group = add_parser.add_mutually_exclusive_group()
    group.add_argument("--id", type=int, help="ID of task")
    group.add_argument("--task", type=str, help="description of an existing task")
    add_parser.add_argument("--status", type=str, help="update the status of a task",
                            choices=["in-progress", "todo", "done"])
    add_parser.add_argument("--new-task", type=str, help="update the task description")
    add_parser.set_defaults(func=update_task_command)

    #delete command
    add_parser = subparser.add_parser("delete", help="delete an existing task")
    add_parser.add_argument("id", type=int, help="ID of task")
    add_parser.set_defaults(func=delete_task_command)

    #reset command
    add_parser = subparser.add_parser("reset", help="resets the task manager")
    add_parser.set_defaults(func=reset_task_command)

    return parser


