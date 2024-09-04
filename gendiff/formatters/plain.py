def format_plain(diff):
    result = []

    def recurse(cur_path, changes):
        for key, change in changes.items():
            new_path = f"{cur_path}.{key}" if cur_path else key
            if change['status'] == 'added':
                value = change['value']
                result.append(f"Property '{new_path}' was added with value: {format_value(value)}")
            elif change['status'] == 'removed':
                result.append(f"Property '{new_path}' was removed")
            elif change['status'] == 'changed':
                old_value = change['old_value']
                new_value = change['new_value']
                result.append(f"Property '{new_path}' was updated. From {format_value(old_value)} to {format_value(new_value)}")
            elif change['status'] == 'nested':
                recurse(new_path, change['value'])

    recurse('', diff)
    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    return value
