#!/usr/bin/env python3


def compare_dicts(dict1, dict2):
    diff = {}
    keys = set(dict1.keys()).union(dict2.keys())
    for key in keys:
        if key in dict1 and key not in dict2:
            diff[key] = {'status': 'removed', 'value': dict1[key]}
        elif key not in dict1 and key in dict2:
            diff[key] = {'status': 'added', 'value': dict2[key]}
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_diff = compare_dicts(dict1[key], dict2[key])
                if nested_diff:
                    diff[key] = {'status': 'nested', 'value': nested_diff}
            elif dict1[key] != dict2[key]:
                diff[key] = {
                    'status': 'changed',
                    'old_value': dict1[key],
                    'new_value': dict2[key]
                }
    return diff
