import pytest
from gendiff import generate_diff


def test_generate_diff(file1, file2, result):
    diff = generate_diff(file1, file2)
    assert diff == result
