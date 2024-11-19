#!/usr/bin/env python3
import json
import yaml
from os.path import splitext


EXTENSIONS = ('yaml', 'yml', 'json')


def load_file(file_path):
    extension = splitext(file_path)[1][1:]
    with open(file_path, 'r') as file:
        content = file.read()
        return content, extension


def parse_data(file_path):
    (content, extension) = load_file(file_path)
    if extension == 'json':
        return json.loads(content)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.load(content, Loader=yaml.Loader)
    else:
        raise ValueError(f'File {file_path} does not end with {extension}')
