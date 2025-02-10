import argparse
from src.commands import (
    add_task_command,
    list_task_command,
    update_task_command,
    delete_task_command,
    reset_task_command
)

def create_subparser(subparsers, name, help_text, func, arguments=None):
    parser = subparsers.add_parser(name, help=help_text)
    if arguments:
        for arg in arguments:
            parser.add_argument(*arg['flags'], **arg['kwargs'])
    parser.set_defaults(func=func)

def setup_parser():
    parser = argparse.ArgumentParser(
        prog="Task Manager CLI",
        description="A task manager to track your tasks"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command configurations
    commands = [
        {
            "name": "add",
            "help": "add task to the tracker",
            "func": add_task_command,
            "arguments": [
                {"flags": ["task"], "kwargs": {"type": str, "help": "Task Description"}},
                {"flags": ["--status"], "kwargs": {"type": str, "choices": ["in-progress", "todo", "done"], "default": "todo", "help": "Current status of task"}},
            ]
        },
        {
            "name": "list",
            "help": "lists current tasks",
            "func": list_task_command,
            "arguments": [
                {"flags": ["--status"], "kwargs": {"type": str, "choices": ["in-progress", "todo", "done", "incomplete"], "help": "choose a status to filter a list"}},
            ]
        },
        {
            "name": "update",
            "help": "update an existing task",
            "func": update_task_command,
            "arguments": [
                {"flags": ["id"], "kwargs": {"type": int, "help": "use the task id to select the task"}},
                {"flags": ["--status"], "kwargs": {"type": str, "choices": ["in-progress", "todo", "done"], "help": "update the status of a task"}},
                {"flags": ["--rename"], "kwargs": {"type": str, "help": "rename the task"}},
            ]
        },
        {
            "name": "delete",
            "help": "delete an existing task",
            "func": delete_task_command,
            "arguments": [
                {"flags": ["id"], "kwargs": {"type": int, "help": "the ID needed to delete the task"}},
            ]
        },
        {
            "name": "reset",
            "help": "resets the task manager",
            "func": reset_task_command,
        }
    ]

    # Apply configurations
    for cmd in commands:
        create_subparser(subparsers, cmd["name"], cmd["help"], cmd["func"], cmd.get("arguments"))

    return parser


