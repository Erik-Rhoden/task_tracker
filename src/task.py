import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self, args):
        self.tasks = []
        self.load_tasks()
        self.description = getattr(args, 'task', None)
        self.status = getattr(args, 'status', None)
        self.id = self.get_id()
        self.createdAt = datetime.now()
        self.updatedAt = None

    def get_id(self):
        if self.tasks:
            return max(task['id'] for task in self.tasks) + 1
        
        return 1

    def load_tasks(self):
        file_path = 'data/tasks.json'
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.tasks = json.load(f)
                if not isinstance(self.tasks, list):
                    self.tasks = []

    def save_tasks(self):
        dir_path = 'data'
        file_path = os.path.join(dir_path, 'tasks.json')

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        task = {
            "description": self.description,
            "status": self.status,
            "id": self.id,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None
        }

        self.tasks.append(task)
    
        with open(file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def get_description(self):
        return f'{self.description}'