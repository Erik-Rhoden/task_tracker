import argparse
from src.commands import add_task_command, list_task_command

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
                            default="in-progress", help="Current status of task")
    add_parser.set_defaults(func=add_task_command)
    
    #list command
    list_parser = subparser.add_parser("list", help="lists current tasks")
    list_parser.set_defaults(func=list_task_command)
    #update command
    #delete command

    return parser


