from src.task import save_tasks, load_tasks, get_description

def add_task_command(tasks):
    save_tasks(tasks)
    print(f'Added task: {tasks.task}')

def list_task_command(tasks):
    tasks = load_tasks()
    
    if not tasks:
        return "no tasks found!"
    
    return get_description(tasks)
