import os
import json
import pytest
from tests import get_path
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    data_1 = 'tests/fixtures/file1.json'
    data_2 = 'tests/fixtures/file2.json'
    data_3 = 'tests/fixtures/file1.yml'
    data_4 = 'tests/fixtures/file2.yml'

    result_stylish = \
        open('tests/fixtures/result_stylish.txt').read()
    result_plain = \
        open('tests/fixtures/result_plain.txt').read()
    result_json = \
        open('tests/fixtures/result_json.txt').read()

    assert generate_diff(data_1, data_2, 'stylish') == result_stylish
    assert generate_diff(data_1, data_2) == result_stylish
    assert generate_diff(data_1, data_2, 'plain') == result_plain
    assert generate_diff(data_1, data_2, 'json') == result_json
