import pytest
import os
from page_loader.page_loader import download, to_file, to_dir
import tempfile
import requests_mock


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


URL = 'https://ru.hexlet.io/courses'
URL2 = 'https://page-loader.hexlet.repl.co/'
IMG2 = 

EXPECTED_HTML = f"{FIXTURES_PATH}/ru-hexlet-io-courses.txt"

DOWNLOADED_HTML = 'ru-hexlet-io-courses.html'


@pytest.mark.parametrize('url, expected_result',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.html')])
def test_download(url, expected_result):
    html_expected = read(EXPECTED_HTML)

    with requests_mock.Mocker() as mock:
        with tempfile.TemporaryDirectory() as tmpdir:
            mock.get(URL, text=html_expected)
            download(URL, tmpdir)
            actual_html = read(os.path.join(tmpdir, DOWNLOADED_HTML))

            assert actual_html == html_expected


def read(file_path):
    with open(file_path, 'r') as data:
        result = data.read()
    return result


@pytest.mark.parametrize('url, expected_filename',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.html')])
def test_to_file(url, expected_filename):
    assert to_file(url) == expected_filename


@pytest.mark.parametrize('url, expected_dir_name',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses_files')])
def test_to_dir(url, expected_dir_name):
    assert to_dir(url) == expected_dir_name



# @pytest.mark.parametrize('file_path, url, res_file_path',
#                          [('./tmp', 'https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.txt')])
# def test_download(url, file_path, res_file_path):
#     fixtures_file = f"{FIXTURES_PATH}/{res_file_path}"
#     with open(fixtures_file, 'r') as data:
#         expected = data.read()
#     result_file = download(file_path, url,  output=os.getcwd())
#     with open(result_file, 'r') as data:
#         result = data.read()
#     assert result == expected
# 
# 
# 
# def get_fixture_path(name):
#     return os.path.join('fixtures', name)
# 
# 
# file_name = 'before.html'
# src = get_fixture_path(file_name)
# 
# 
# @pytest.fixture(scope='module')
# def expected():
#     return read(get_fixture_path('after.html'))
# 
# 
# @pytest.fixture
# def dest_file(tmpdir):
#     dest = tmpdir.join(file_name)
#     shutil.copyfile(src, dest)
#     return dest
# 
# 
# def test_prettify(dest_file, expected):
#     prettify_html_file(dest_file)
#     actual = read(dest_file)
    # assert actual == expected