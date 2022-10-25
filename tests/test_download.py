import pytest
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
    html_original = read(HTML_ORIGINAL, 'r')
    html_expected = read(HTML_PRETTIFY, 'r')

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        resources = TEST_DATA
        mock.get(URL, text=html_original)
        for url, path in resources:
            content = read(path, 'rb')
            mock.get(url, content=content)
        download(URL, tmpdir)
        actual_html = read(os.path.join(tmpdir, to_filename(URL)), 'r')
        assert actual_html == html_expected
        assert mock.call_count == 5


def test_prepare_data():
    html_original = read(HTML_ORIGINAL, 'r')
    html_expected = read(HTML_PRETTIFY, 'r')

    with requests_mock.Mocker() as mock:
        mock.get(URL, text=html_original)
        resources, html = prepare_data(URL)
        expected_resources = [
            ('/assets/professions/nodejs.png',
             'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-professions-nodejs.png'),
            ('/assets/application.css',
             'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-application.css'),
            ('/courses',
             'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-courses.html'),
            ('/script.js',
             'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-script.js')
        ]
        assert html_expected == html
        assert expected_resources == resources


def read(file_path, mode):
    with open(file_path, mode) as data:
        return data.read()


def test_exception():
    with pytest.raises(Exception) as e:
        download('https://notexist.com')

        assert str(e.value) == requests.RequestException


def test_directory_not_exist():
    try:
        download(URL, 'some_dir')
    except FileNotFoundError:
        print("Directory 'some_dir' doesn't exist")
