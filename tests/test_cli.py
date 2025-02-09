import subprocess
import os
import shutil

class TestAddTask:
    def test_add_task_cli(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_py = os.path.join(project_root, "main.py")

        result = subprocess.run(
            ["python3", main_py, "add", "new task"],
            capture_output=True, text=True
        )

        assert result.returncode == 0
        assert "Added task: new task" in result.stdout

    def test_add_task_cli_fail(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_py = os.path.join(project_root, "main.py")

        result = subprocess.run(
            ["python3", main_py, "add"],
            capture_output=True, text=True
        )

        assert result.returncode == 2
    
class TestListTask:
    def test_no_list(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_py = os.path.join(project_root, "main.py")

        data_dir = os.path.join(project_root, 'data')       
        data_dir = os.path.abspath(data_dir) 

        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)

        result = subprocess.run(
            ["python3", main_py, "list"],
            capture_output=True, text=True
        )

        assert result.returncode == 0
        assert "no tasks found!" in result.stdout

    def test_list(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        main_py = os.path.join(project_root, "main.py")

        subprocess.run(
            ["python3", main_py, "add", "new task"],
            capture_output=True, text=True
        )

        result = subprocess.run(
            ["python3", main_py, "list"],
            capture_output=True, text=True
        )

        assert result.returncode == 0
        assert not "no tasks found!" in result.stdout
