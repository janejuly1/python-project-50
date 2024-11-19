from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import stylish_diff
from gendiff.formatters.json_formatter import json_formatter
from gendiff.data_converter import parse_data
from gendiff.compare_files import compare_dicts


FORMATTERS = {
    'stylish': stylish_diff,
    'plain': format_plain,
    'json': json_formatter
}


def generate_diff(filepath1, filepath2, format_name='stylish'):
    dict1 = parse_data(filepath1)
    dict2 = parse_data(filepath2)

    diff = compare_dicts(dict1, dict2)

    format_name = FORMATTERS[format_name]

    output = format_name(diff)
    return output
