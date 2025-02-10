#!/usr/bin/env python3

from src.cli import setup_parser
from src.task import make_json_file


def main():
    make_json_file()

    parser = setup_parser()
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()
