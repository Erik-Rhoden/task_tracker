import subprocess

class TestAddTask:
    def test_add_task_cli(self):
        result = subprocess.run(
            ["python3", "main.py", "add", "new task"],
            capture_output=True, text=True
        )

        assert result.returncode == 0
        assert "Added task: new task" in result.stdout

    def test_add_task_cli_fail(self):
        result = subprocess.run(
            ["python3", "main.py", "add"],
            capture_output=True, text=True
        )

        assert result.returncode == 2
    