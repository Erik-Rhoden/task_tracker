import os
import json
from datetime import datetime
import shutil
import textwrap

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')

# create data/tasks.json if it does not exist
def make_tasks_file():
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        if not os.path.isfile(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                json.dump([], f, indent=4)

    except Exception as e:
        print(e)

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
    
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

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

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def update_task_status(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['task'] == arg.task:
            old_task = task['task']
            task['status'] = arg.status
            task['updatedAt'] = datetime.now().isoformat()
            print(f'{old_task} status updated to {arg.status}')
            break
    
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

#updates the status of an individual task by id
def update_id_new_task(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == arg.id:
            task['task'] = arg.new_task
            task['updatedAt'] = datetime.now().isoformat()
            print(f'ID {task['id']} updated to {arg.new_task}')
            break

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def update_task_new_task(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['task'] == arg.task:
            old_task = task['task']
            task['task'] = arg.new_task
            task['updatedAt'] = datetime.now().isoformat()
            print(f'{old_task} updated to {arg.new_task}')
            break

    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

#deletes a task
def delete_task(arg):
    tasks = load_tasks()

    if not tasks:
        print("no tasks available!")
        return
        
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

    with open(TASKS_FILE, 'w') as f:
        json.dump(new_tasks, f, indent=4)

#deletes data/tasks.json 
def reset_task(arg):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_root, 'data')   

    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
        print('The task manager has been reset')

#helper function for list command
def get_description(tasks):
    if not tasks:
        return
    
    headers = ["ID", "TASKS", "STATUS"]

    print("{: <5} {: <30} {: <15}".format(*headers))
    print("-" * 65)

    for task in tasks:
        wrapped_task = textwrap.wrap(task['task'], width=30)
        print("{: <5} {: <30} {: <15}".format(str(task['id']), wrapped_task[0], task['status']))

        for line in wrapped_task[1:]:
            print("{:<5} {:<30} {:<15}".format("", line, ""))
