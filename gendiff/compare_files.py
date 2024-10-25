def compare_dicts(dict1, dict2):
    diff = {}
    keys = set(dict1) | set(dict2)

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if key not in dict1:
            diff[key] = {'status': 'added', 'value': value2}
        elif key not in dict2:
            diff[key] = {'status': 'removed', 'value': value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
            nested_diff = compare_dicts(value1, value2)
            if nested_diff:
                diff[key] = {'status': 'nested', 'value': nested_diff}
        elif value1 != value2:
            diff[key] = {
                'status': 'changed',
                'old_value': value1,
                'new_value': value2
            }
        else:
            diff[key] = {
                'status': 'unchanged',
                'value': value1
            }

    return diff
