import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self, args):
        self.tasks = {}
        self.description = getattr(args, 'task', None)
        self.status = getattr(args, 'status', None)
        self.id = 1
        self.createdAt = datetime.now()
        self.updatedAt = None

    def load_tasks(self):
        if os.path.exists("data/tasks.json"):
            with open('data/tasks.json', "r") as f:
                data = json.load(f)
                print(data)
        else:
            print("No such directory!")

    def get_description(self):
        return f'{self.description}'