import os
import shutil
import pytest
from src.task import make_tasks_file
from src.paths import DATA_DIR, TASKS_FILE

@pytest.fixture(scope="function", autouse=True)
def remove_data_dir():
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)    

    yield

    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)

class TestTask():
    def test_make_tasks_file(self):
        make_tasks_file()

        assert os.path.exists(TASKS_FILE)
