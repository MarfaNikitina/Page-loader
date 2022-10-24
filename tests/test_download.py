import pytest
# from urllib.parse import urlparse
import os
from page_loader.url import to_filename, to_dir
from page_loader.page_loader import download
import tempfile
import requests
import requests_mock
from page_loader.resources import prepare_data

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"

TEST_DATA = [
    ('https://page-loader.hexlet.repl.co/assets/professions/nodejs.png',
        f"{FIXTURES_PATH}/fixture_img.png"),
    ('https://page-loader.hexlet.repl.co/assets/application.css',
     f"{FIXTURES_PATH}/fixture_css.css"),
    ('https://page-loader.hexlet.repl.co/script.js',
        f"{FIXTURES_PATH}/fixture_scripts.js"),
    ('https://page-loader.hexlet.repl.co/courses',
        f"{FIXTURES_PATH}/fixture_courses.txt")
]

URL = 'https://page-loader.hexlet.repl.co/'
HTML_ORIGINAL = f"{FIXTURES_PATH}/original_html.html"
HTML_PRETTIFY = f"{FIXTURES_PATH}/prettify_html.html"


def test_download():
    html_original = read(HTML_ORIGINAL)
    html_expected = read(HTML_PRETTIFY)

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        resources = TEST_DATA
        mock.get(URL, text=html_original)
        for resource in resources:
            mock.get(resource[0])
        download(URL, tmpdir)
        actual_html = read(os.path.join(tmpdir, to_filename(URL)))
        assert actual_html == html_expected
        assert mock.call_count == 5


def test_prepare_data():
    html_original = read(HTML_ORIGINAL)
    html_expected = read(HTML_PRETTIFY)

    with requests_mock.Mocker() as mock:
        mock.get(URL, text=html_original)
        resources, html = prepare_data(URL, to_dir(URL))
        expected_resources = [
            '/assets/application.css',
            '/courses',
            '/assets/professions/nodejs.png',
            '/script.js']

        assert html_expected == html
        assert expected_resources == resources


def read(file_path, binary=False):
    if binary:
        with open(file_path, 'rb') as data:
            return data.read()
    else:
        with open(file_path, 'r') as data:
            return data.read()


def test_false_response():
    with pytest.raises(Exception) as e:
        download('https://notexist.com')

        assert str(e.value) == requests.RequestException
