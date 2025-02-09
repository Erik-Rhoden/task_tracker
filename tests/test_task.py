import os
import shutil
import pytest
from src.task import make_tasks_file

@pytest.fixture
def remove_data_dir():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(project_root, 'data')   

    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)    

    yield 

class TestTask():
    def test_make_tasks_file(self, remove_data_dir):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(project_root, 'data', 'tasks.json')

        make_tasks_file()

        assert os.path.exists(data_path)
