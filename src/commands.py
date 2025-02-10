from src.task import save_tasks, load_tasks, get_description, update_status, update_task, delete_task, reset_task

def add_task_command(tasks):
    save_tasks(tasks)

def list_task_command(tasks):
    record = load_tasks()
    
    if not record:
        print("no tasks found!")
    
    return get_description(record)

def update_task_command(arg):
    if arg.status:
        update_status(arg)

    if arg.new_task:
        update_task(arg)

def delete_task_command(arg):
    delete_task(arg)

def reset_task_command(arg):
    reset_task(arg)
    
