def format_plain(diff):
    lines = plain_formatter(diff)
    result = '\n'.join(lines)
    return result


def plain_formatter(diff, path=""):
    lines = []

    def add_line(status, value, full_key):
        actions = {
            "nested": lambda value, full_key: lines.extend(
                plain_formatter(value, full_key)
            ),
            "added": lambda value, full_key: lines.append(
                format_added_property(value, full_key)
            ),
            "removed": lambda value, full_key: lines.append(
                f"Property '{full_key}' was removed"
            ),
            "changed": lambda value, full_key: lines.append(
                format_changed_property(value, full_key)
            ),
            "unchanged": lambda value, full_key: None
        }
        action = actions.get(status)
        if action:
            action(value, full_key)

    sorted_diff = []
    for k, v in diff.items():
        sorted_diff.append((k, v, create_full_key(path, k)))

    sorted_diff.sort(key=lambda x: x[2])

    for (key, value, full_key) in sorted_diff:
        status = value.get('status')

        if 'value' in value:
            v = value['value']
        elif 'old_value' in value and 'new_value' in value:
            v = (value['old_value'], value['new_value'])
        else:
            v = None

        add_line(status, v, full_key)

    return lines


def create_full_key(path, key):
    if path == "":
        full_key = f"{key}"
    else:
        full_key = f"{path}.{key}"
    return full_key


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()


def format_added_property(value, full_key):
    value = format_value(value)
    if isinstance(value, dict):
        value_description = "[complex value]"
    elif isinstance(value, str):
        value_description = f"{value}"
    else:
        value_description = str(value).lower()
    message = (
        f"Property \'{full_key}\' was added with value: {value_description}"
    )
    return message


def format_changed_property(value, full_key):
    old, new = value
    old, new = format_value(old), format_value(new)
    if isinstance(old, dict):
        old_value = "[complex value]"
    elif isinstance(old, str):
        old_value = f"{old}"
    else:
        old_value = str(old).lower()
    if isinstance(new, dict):
        new_value = "[complex value]"
    elif isinstance(new, str):
        new_value = f"{new}"
    else:
        new_value = str(new).lower()
    message = (
        f"Property \'{full_key}\' was updated. From {old_value} to {new_value}"
    )
    return message
