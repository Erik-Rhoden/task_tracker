import os
import json
from datetime import datetime
import shutil

# create data/tasks.json if it does not exist
def make_tasks_file():
    try:
        if not os.path.exists('data'):
            os.makedirs('data')

        file_path = 'data/tasks.json'

        if not os.path.exists(file_path):
            with open(file_path, 'a+') as f:
                json.dump([], f)

    except Exception as e:
        print(e)

# checks for max id and returns id
def create_id():
    arr = []

    if os.path.getsize('data/tasks.json') == 0:
        return 1
    
    with open('data/tasks.json') as data_file:
        data = json.load(data_file)
        for task in data:
            arr.append(task['id'])
    return max(arr) + 1 if arr else 1
    
#loads tasks.json if file exists
def load_tasks():
    with open('data/tasks.json', "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

#updates tasks.json with new tasks
def save_tasks(args):
    tasks = load_tasks()

    task = {
        "task": args.task,
        "status": args.status,
        "id": create_id(),
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(task)
    
    with open('data/tasks.json', "w") as f:
        json.dump(tasks, f, indent=4)

    print(f'Task added successfully (ID: {task['id']})')

#updates the status of an individual task by id
def update_status(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == arg.id or task['task'] == arg.task:
            task['status'] = arg.status
            task['updatedAt'] = datetime.now().isoformat()
            print(f'{task['task']} status updated to {arg.status}')
            break

    with open('data/tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

#updates the status of an individual task by id
def update_task(arg):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == arg.id or task['task'] == arg.task:
            task['task'] = arg.new_task
            task['updatedAt'] = datetime.now().isoformat()
            print(f'ID {task['id']} updated to {arg.new_task}')
            break

    with open('data/tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

#deletes a task
def delete_task(arg):
    tasks = load_tasks()

    if not tasks:
        print("no tasks available!")
        
    new_tasks = []

    for task in tasks:
        if task['id'] != arg.id:
            new_tasks.append(task)
        else:
            print(f'{task['task']} has been deleted')

    with open('data/tasks.json', 'w') as f:
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
    for task in tasks:
        print(f'ID: {task['id']}')
        print(f'Task: {task['task']}')
        print(f'Status: {task['status']}')
        print(f'CreatedAt: {task['createdAt']}')
        print(f'UpdatedAt: {task['updatedAt']}\n')
