from src.task import save_tasks, load_tasks, get_description, update_status, update_task

def add_task_command(tasks):
    save_tasks(tasks)
    print(f'Added task: {tasks.task}')

def list_task_command(tasks):
    record = load_tasks()
    
    if not record:
        print("no tasks found!")
    
    return get_description(record)

def update_task_command(arg):
    if arg.status:
        update_status(arg)

    if arg.task:
        update_task(arg)
    
