from src.task import TaskManager

def add_task_command(tasks):
    print(f'Added task: {tasks.description}')

def list_task_command(tasks):
    tasks.load_tasks()