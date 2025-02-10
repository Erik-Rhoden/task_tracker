#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.cli import setup_parser
from src.task import make_tasks_file

def main():
    make_tasks_file()

    parser = setup_parser()
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()
