#!/usr/bin/env python3
import argparse
import json
import yaml
from formatters.plain import format_plain
from formatters.stylish import stylish_diff



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


def load_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)


def compare_dicts(dict1, dict2):
    diff = {}
    keys = set(dict1.keys()).union(dict2.keys())
    for key in keys:
        if key in dict1 and key not in dict2:
            diff[key] = {'status': 'removed', 'value': dict1[key]}
        elif key not in dict1 and key in dict2:
            diff[key] = {'status': 'added', 'value': dict2[key]}
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_diff = compare_dicts(dict1[key], dict2[key])
                if nested_diff:
                    diff[key] = {'status': 'nested', 'value': nested_diff}
            elif dict1[key] != dict2[key]:
                diff[key] = {
                    'status': 'changed',
                    'old_value': dict1[key],
                    'new_value': dict2[key]
                }
    return diff


def generate_diff(filepath1, filepath2, format_name='stylish'):
    dict1 = load_file(filepath1)
    dict2 = load_file(filepath2)

    diff = compare_dicts(dict1, dict2)

    if format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'stylish':
        return stylish_diff(diff)

    output = '{\n' + stylish_diff(diff) + '\n}'
    return output


if __name__ == '__main__':
    args = gendiff()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
