#!/usr/bin/env python3

from ..formatters.plain import format_plain
from ..formatters.stylish import stylish_diff
from ..data_converter import load_file
from ..cli import pars_params
from ..compare_files import compare_dicts


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
    args = pars_params()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
