#!/usr/bin/env python3
import argparse
import json
import yaml


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


def format_diff(diff):
    lines = []
    for key in diff:
        if diff[key]['status'] == 'added':
            lines.append(f'  + {key}: {diff[key]["value"]}')
        elif diff[key]['status'] == 'removed':
            lines.append(f'  - {key}: {diff[key]["value"]}')
        elif diff[key]['status'] == 'changed':
            lines.append(f'  - {key}: {diff[key]["old_value"]}')
            lines.append(f'  + {key}: {diff[key]["new_value"]}')
        elif diff[key]['status'] == 'nested':
            lines.append(f'  {key}: {format_diff(diff[key]["value"])})')
    return '\n'.join(lines)


def generate_diff(filepath1, filepath2):
    dict1 = load_file(filepath1)
    dict2 = load_file(filepath2)

    diff = compare_dicts(dict1, dict2)

    output = '{\n' + format_diff(diff) + '\n}'
    return output

# def generate_diff(file1, file2):
#     with open(file1) as f1, open(file2) as f2:
#         data1 = json.load(f1)
#         data2 = json.load(f2)
#
#     diff = []
#
#     keys = set(data1.keys()).union(data2.keys())
#
#     for key in sorted(keys):
#         if key not in data2:
#             diff.append(f"- {key}: {data1[key]}")
#         elif key not in data1:
#             diff.append(f"+ {key}: {data2[key]}")
#         elif data1[key] != data2[key]:
#             diff.append(f"- {key}: {data1[key]}")
#             diff.append(f"+ {key}: {data2[key]}")
#         elif data1[key] == data2[key]:
#             diff.append(f"  {key}: {data1[key]}")
#         else:
#             if isinstance(data1[key], dict) and isinstance(data2[key], dict):
#                 nested_diff = generate_diff(data1[key], data2[key])
#
#     ret = "\n".join(diff)
#     return "{\n" + ret + "\n}"


if __name__ == '__main__':
    args = gendiff()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
