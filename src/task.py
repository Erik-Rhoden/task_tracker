import os
import json
from datetime import datetime
import shutil
import textwrap
from src.paths import DATA_DIR, TASKS_FILE

# create data/tasks.json if it does not exist
def make_json_file():
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.isfile(TASKS_FILE) or not is_valid_json(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                json.dump([], f, indent=4)

    except Exception as e:
        raise RuntimeError(f"Failed to create tasks file: {e}")
    
def is_valid_json(TASKS_FILE):
    try:
        with open(TASKS_FILE, 'r') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, FileNotFoundError):
        return False

# checks for max id and returns id
def create_id():
    arr = []

    if os.path.getsize(TASKS_FILE) == 0:
        return 1
    
    with open(TASKS_FILE) as data_file:
        data = json.load(data_file)
        for task in data:
            arr.append(task['id'])
    return max(arr) + 1 if arr else 1
    
#loads tasks.json if file exists
def load_tasks():
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

#updates tasks.json with new tasks
def save_tasks(args):
    tasks = load_tasks()

    task = {
        "id": create_id(),
        "task": args.task,
        "status": args.status,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(task)
    
    write_json_file(tasks)

    print(f'Task added successfully (ID: {task['id']})')

#updates the status of an individual task by id
def update_id_status(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == arg.id:
            task['status'] = arg.status
            task['updatedAt'] = datetime.now().isoformat()
            print(f'ID {task['id']} status updated to {arg.status}')
            break

    write_json_file(tasks)

#updates the status of an individual task by id
def update_id_new_task(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == arg.id:
            task['task'] = arg.rename
            task['updatedAt'] = datetime.now().isoformat()
            print(f'ID {task['id']} updated to {arg.rename}')
            break

    write_json_file(tasks)

#deletes a task
def delete_task(arg):
    tasks = load_tasks()
        
    new_tasks = []
    task_found = False

    for task in tasks:
        if task['id'] == arg.id:
            task_found = True
            print(f'{task['task']} has been deleted')
        else:
            new_tasks.append(task)
    
    if not task_found:
        print('no such task!')
        return
    
    write_json_file(new_tasks)

#deletes data/tasks.json 
def reset_task():
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)
        print('The task manager has been reset')

#helper function for list command
def get_list(arg):
    record = load_tasks()

    if not record:
        print("no tasks found!")
        return

    headers = ["ID", "TASKS", "STATUS"]

    print("{: <5} {: <30} {: <15}".format(*headers))
    print("-" * 45)

    if arg.status == "incomplete":
        for task in record:
            if task['status'] == "done":
                continue
            
            wrapped_task = textwrap.wrap(task['task'], width=30)
            print("{: <5} {: <30} {: <15}".format(str(task['id']), wrapped_task[0], task['status']))

            for line in wrapped_task[1:]:
                print("{:<5} {:<30} {:<15}".format("", line, ""))
    else:
        for task in record:
            if arg.status and task['status'] != arg.status:
                continue

            wrapped_task = textwrap.wrap(task['task'], width=30)
            print("{: <5} {: <30} {: <15}".format(str(task['id']), wrapped_task[0], task['status']))

            for line in wrapped_task[1:]:
                print("{:<5} {:<30} {:<15}".format("", line, ""))

def write_json_file(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
