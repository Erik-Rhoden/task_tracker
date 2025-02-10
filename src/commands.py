from src.task import (
    save_tasks, 
    get_list, 
    update_id_status, 
    update_id_new_task, 
    delete_task, 
    reset_task
)

def add_task_command(tasks):
    save_tasks(tasks)

def list_task_command(arg):
    return get_list(arg)

def update_task_command(arg):
    if arg.id and arg.status:
        update_id_status(arg)

    if arg.id and arg.new_name:
        update_id_new_task(arg)
        
def delete_task_command(arg):
    delete_task(arg)

def reset_task_command(arg):
    reset_task()
    
