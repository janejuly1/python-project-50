#!/usr/bin/env python3

from gendiff.cli import parse_params
from .diff import generate_diff


def main():
    args = parse_params()
    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
    except ValueError:
        print('File does not end with right extension')
    print(diff)


if __name__ == '__main__':
    main()
