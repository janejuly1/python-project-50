import pytest
from tests import get_path
from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, format_name, expected,',
                         [
                             pytest.param(
                                 'file1.json',
                                 'file2.json',
                                 'stylish',
                                 'result.txt',
                                 id="json_file"
                             ),
                             pytest.param(
                                 'file1.yaml',
                                 'file2.yaml',
                                 'stylish',
                                 'correct_result.txt',
                                 id="yaml_file"
                             ),
                             pytest.param(
                                 'file1.yaml',
                                 'file2.json',
                                 'stylish',
                                 'result.txt',
                                 id="mix_file"
                             ),
                             pytest.param(
                                 'empty_file.json',
                                 'empty_file.json',
                                 'stylish',
                                 'result_empty.txt',
                                 id="empty_file"
                             ),
                             pytest.param(
                                 'file1.yaml',
                                 'file2.yaml',
                                 'plain',
                                 'result_plain.txt',
                                 id="plain"
                             ),
                             pytest.param(
                                 'file1.json',
                                 'file2.json',
                                 'json',
                                 'result_json.txt',
                                 id="json"
                             ),
                         ])
def test_generate_diff(file1, file2, format_name, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result = file.read()
        test_path1 = get_path(file1)
        test_path2 = get_path(file2)
        assert generate_diff(test_path1, test_path2, format_name) == result
