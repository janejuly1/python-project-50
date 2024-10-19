import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'plain',
     "tests/fixtures/result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish',
     "tests/fixtures/result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'stylish',
     "tests/fixtures/result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'plain',
     "tests/fixtures/result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json',
     "tests/fixtures/result_json.json"),
])
def test_generate_diff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
