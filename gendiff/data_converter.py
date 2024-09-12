#!/usr/bin/env python3
import json
import yaml


def load_file(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
