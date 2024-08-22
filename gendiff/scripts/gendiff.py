#!/usr/bin/env python3
import argparse
import json


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish', type=str
    )
    return parser.parse_args()


def generate_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = []

    keys = set(data1.keys()).union(data2.keys())

    for key in sorted(keys):
        if key not in data2:
            diff.append(f"- {key}: {data1[key]}")
        elif key not in data1:
            diff.append(f"+ {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"- {key}: {data1[key]}")
            diff.append(f"+ {key}: {data2[key]}")
        else:
            diff.append(f"  {key}: {data1[key]}")

    ret = "\n".join(diff)
    return "{\n" + ret + "\n}"


if __name__ == '__main__':
    args = gendiff()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
