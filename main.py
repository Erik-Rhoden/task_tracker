from src.cli import setup_parser
from src.task import TaskManager

def main():
    parser = setup_parser()
    args = parser.parse_args()

    tasks = TaskManager(args)

    if hasattr(args, "func"):
        args.func(tasks)

if __name__ == '__main__':
    main()