import pytest
import os
from page_loader.page_loader import download
import requests
# import requests_mock


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize('file_path, url, res_file_path',
                         [('./tmp', 'https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.txt')])
def test_download(url, file_path, res_file_path):
    fixtures_file = f"{FIXTURES_PATH}/{res_file_path}"
    with open(fixtures_file, 'r') as data:
        expected = data.read()
    result_file = download(file_path, url,  output=os.getcwd())
    with open(result_file, 'r') as data:
        result = data.read()
    assert result == expected
