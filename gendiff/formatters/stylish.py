def stylish_diff(diff):
    def format_value(value):
        if isinstance(value, dict):
            return '{\n' + stylish_diff(value) + '\n}'
        return value

    lines = []
    for key, change in diff.items():
        if change['status'] == 'added':
            lines.append(f'  + {key}: {format_value(change["value"])}')
        elif change['status'] == 'removed':
            lines.append(f'  - {key}: {format_value(change["value"])}')
        elif change['status'] == 'changed':
            lines.append(f'  - {key}: {format_value(change["old_value"])}')
            lines.append(f'  + {key}: {format_value(change["new_value"])}')
        elif change['status'] == 'nested':
            lines.append(f'  {key}: {stylish_diff(change["value"])}')
        elif change['status'] == 'unchanged':
            lines.append(f'    {key}: {format_value(change["value"])}')

    return '\n'.join(lines)
