from src.task import (
    save_tasks, load_tasks, get_list, update_id_status, 
    update_id_new_task, update_task_new_task, update_task_status, 
    delete_task, reset_task
)

def add_task_command(tasks):
    save_tasks(tasks)

def list_task_command(tasks):
    return get_list()

def update_task_command(arg):
    if arg.id and arg.status:
        update_id_status(arg)

    if arg.id and arg.new_task:
        update_id_new_task(arg)

    if arg.task and arg.new_task:
        update_task_new_task(arg)

    if arg.task and arg.status:
        update_task_status(arg)
        
def delete_task_command(arg):
    delete_task(arg)

def reset_task_command(arg):
    reset_task()
    
