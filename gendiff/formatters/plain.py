
def format_plain(diff):
    return '\n'.join(plain_formatter(diff))


def plain_formatter(diff, path=""):
    lines = []

    actions = {
        "nested": lambda value, full_key: lines.extend(plain_formatter(value, full_key)),
        "added": lambda value, full_key: lines.append(format_added_property(value, full_key)),
        "removed": lambda value, full_key: lines.append(f"Property '{full_key}' was removed"),
        "changed": lambda value, full_key: lines.append(format_changed_property(value, full_key)),
        "unchanged": lambda value, full_key: None
    }

    for key, (status, value) in diff.items():
        full_key = create_full_key(path, key)
        action = actions.get(status)
        if action:
            action(value, full_key)

    return lines


def create_full_key(path, key):
    return f"{path}.{key}" if path else key


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    return str(value).lower()


def format_added_property(value, full_key):
    value_description = format_value(value)
    return f"Property '{full_key}' was added with value: {value_description}"


def format_changed_property(value, full_key):
    old, new = map(format_value, value)
    return f"Property '{full_key}' was updated. From {old} to {new}"
