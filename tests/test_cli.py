import subprocess
import os
import shutil
import pytest
from src.paths import DATA_DIR, PROJECT_ROOT

main_py = os.path.join(PROJECT_ROOT, "main.py")

@pytest.fixture(scope="function")
def remove_data_dir():
    print(f"DEBUG: DATA_DIR = {DATA_DIR}")

    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)    

    yield

    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR) 


class TestAddTask:
    def test_add_task_cli(self, remove_data_dir):
        result = subprocess.run(
            ["python3", main_py, "add", "new task"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "Task added successfully (ID: 1)\n" in result.stdout

    def test_add_task_cli_fail(self):
        result = subprocess.run(
            ["python3", main_py, "add"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )

        assert result.returncode == 2
    
class TestListTask:
    def test_no_list(self, remove_data_dir):
        result = subprocess.run(
            ["python3", main_py, "list"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )

        assert result.returncode == 0
        assert "no tasks found!" in result.stdout

    def test_list(self):
        subprocess.run(
            ["python3", main_py, "add", "new task"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        result = subprocess.run(
            ["python3", main_py, "list"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert not "no tasks found!" in result.stdout

class TestUpdate:
    def test_update_status_id(self):
        #update status using task id
        subprocess.run(
            ["python3", main_py, "add", "test"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        result = subprocess.run(
            ["python3", main_py, "update", "--id", "1", "--status", "todo"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "ID 1 status updated to todo\n" in result.stdout

    def test_update_task_id(self):
        result = subprocess.run(
            ["python3", main_py, "update", "--id", "1", "--new-task", "new test"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "ID 1 updated to new test" in result.stdout

    def test_update_status_task(self):
        result = subprocess.run(
            ["python3", main_py, "update", "--task", "new test", "--status", "in-progress"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "new test status updated to in-progress" in result.stdout

    def test_update_task_new_task(self):
        result = subprocess.run(
            ["python3", main_py, "update", "--task", "new test", "--new-task", "test"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "new test updated to test" in result.stdout

class TestDelete:
    def test_delete(self):
        subprocess.run(
            ["python3", main_py, "add", "test"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        result = subprocess.run(
            ["python3", main_py, "delete", "1"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "test has been deleted" in result.stdout

    def test_delete_fail(self):
        result = subprocess.run(
            ["python3", main_py, "delete", "10"],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=True
        )

        assert result.returncode == 0
        assert "no such task!" in result.stdout
