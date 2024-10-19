#!/usr/bin/env python3

from ..formatters.plain import format_plain
from ..formatters.stylish import stylish_diff
from ..formatters.json_formatter import json_formatter
from ..data_converter import load_file
from ..cli import parse_params
from ..compare_files import compare_dicts


FORMATTERS = {
    'stylish': stylish_diff,
    'plain': format_plain,
    'json': json_formatter
}


def generate_diff(filepath1, filepath2, format_name='stylish'):
    dict1 = load_file(filepath1)
    dict2 = load_file(filepath2)

    diff = compare_dicts(dict1, dict2)

    if isinstance(format_name, str):
        format_name = FORMATTERS[format_name]

    output = format_name(diff)
    return output


def main():
    args = parse_params()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
