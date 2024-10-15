def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = [
            f"{build_indent(depth + 1)}  {key}: {format_value(val, depth + 1)}"
            for key, val in value.items()
        ]
        return f"{{\n{'\n'.join(lines)}\n{build_indent(depth)}}}"
    elif isinstance(value, list):
        lines = [
            f"{build_indent(depth + 1)}- {format_value(val, depth + 1)}"
            for val in value
        ]
        return f"[\n{'\n'.join(lines)}\n{build_indent(depth)}]"
    return stringify(value)


def stringify(data):
    if isinstance(data, bool):
        return 'true' if data else 'false'
    if data is None:
        return 'null'
    return str(data)


def format_dict(diff, depth=1):
    if not isinstance(diff, dict):
        return str(diff)

    lines = []
    for item in diff:
        key = item['key']
        status = item['status']
        value = item['value']
        indent = build_indent(depth)

        if status == 'added':
            lines.append(f"{indent}+ {key}: {format_value(value, depth)}")
        elif status == 'removed':
            lines.append(f"{indent}- {key}: {format_value(value, depth)}")
        elif status == 'changed':
            old_value, new_value = value
            lines.append(f"{indent}- {key}: {format_value(old_value, depth)}")
            lines.append(f"{indent}+ {key}: {format_value(new_value, depth)}")
        elif status == 'unchanged':
            lines.append(f"{indent}  {key}: {format_value(value, depth)}")

    return '\n'.join(lines)


def stylish_diff(diff):
    return '\n' + format_dict(diff) + '\n'
