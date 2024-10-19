def stylish_diff(diff):
    result = '{\n' + tree_view(diff) + '\n}'
    return result


def tree_view(diff, depth=1):
    lines = []
    for key, value in sorted(diff.items()):
        status = value.get('status')

        if 'value' in value:
            v = value['value']
        elif 'old_value' in value and 'new_value' in value:
            v = (value['old_value'], value['new_value'])
        else:
            v = None

        lines = create_formatted_line(lines, key, v, depth, status)
    result = '\n'.join(lines)
    return result


def create_formatted_line(lines, key, value, depth, status):
    prefix = '  '
    if status == 'nested':
        lines.append(f"{' ' * (4 * depth)}{key}: {{")
        child_diff = tree_view(value, depth + 1)
        lines.append(child_diff)
        lines.append(f"{' ' * (4 * depth)}}}")
    elif status == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif status == 'added':
        prefix = '+ '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    elif status == 'removed':
        prefix = '- '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    else:
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    return lines


def add_indent_and_format(depth, lines, prefix, key, value):
    formated_value = format_value(value, depth + 1)
    indent = (4 * depth - 2) * ' '
    lines.append(f"{indent}{prefix}{key}: {formated_value}")
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            formated_value = format_value(val, depth + 1)
            lines = add_indent_and_format(depth, lines,
                                          prefix, key, formated_value)
        indent = ' ' * (4 * (depth - 1))
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return value


def changed_data_diff(lines, value, depth, key):
    old, new = value
    old_new_pairs = [('- ', old), ('+ ', new)]
    for prefix, value in old_new_pairs:
        formated_value = format_value(value, depth + 1)
        lines = add_indent_and_format(depth, lines, prefix, key, formated_value)
    return lines
