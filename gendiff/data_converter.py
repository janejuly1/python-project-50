import json
import yaml
from os.path import splitext


EXTENSIONS = ('yaml', 'yml', 'json')


def load_file(file_path):
    extension = splitext(file_path)[1][1:]
    if extension in EXTENSIONS:
        with open(file_path, 'r') as file:
            content = file.read()
        return content, extension
    else:
        raise ValueError(f'File {file_path} does not end with {extension}')


def check_file(content, extension):
    content, extension = load_file(content)
    if extension == 'json':
        return json.loads(content)
    elif extension == 'yaml' or extension == 'yml':
        return yaml.load(content, Loader=yaml.Loader)


def parse_data(file_path):
    file_format = splitext(file_path)[1][1:]
    return check_file(file_path, file_format)
