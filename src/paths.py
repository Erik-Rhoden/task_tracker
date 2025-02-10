import os
import sys

if getattr(sys, 'frozen', False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
elif 'pytest' in sys.modules:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
else:
    PROJECT_ROOT = os.path.dirname(os.path.realpath(sys.argv[0]))

DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')
