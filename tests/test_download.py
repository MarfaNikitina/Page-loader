import pytest
import os
from page_loader.name import to_filename, to_dir
from page_loader.page_loader import download
import tempfile
import requests_mock
from page_loader.resources import get_resources

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


# URL1 = 'https://ru.hexlet.io/courses'
URL = 'https://page-loader.hexlet.repl.co/'
IMG_URL = 'https://page-loader.hexlet.repl.co/assets/professions/nodejs.png'
CSS_URL = 'https://page-loader.hexlet.repl.co/assets/application.css'
JS_URL = 'https://page-loader.hexlet.repl.co/script.js'
COURSES_URL = 'https://page-loader.hexlet.repl.co/courses'

EXPECTED_COURSES = f"{FIXTURES_PATH}/fixture_courses.txt"
ORIGINAL_HTML = f"{FIXTURES_PATH}/original_html.html"
EXPECTED_HTML = f"{FIXTURES_PATH}/prettify_html.html"
EXPECTED_IMG = f"{FIXTURES_PATH}/fixture_img.png"
EXPECTED_CSS = f"{FIXTURES_PATH}/fixture_css.css"
EXPECTED_JS = f"{FIXTURES_PATH}/fixture_scripts.js"


DOWNLOADED_HTML = 'page-loader-hexlet-repl-co-.html'
DOWNLOADED_TXT = 'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--courses'
DOWNLOADED_IMG = 'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--assets-professions-nodejs.png'
DOWNLOADED_CSS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--assets-application.css"
DOWNLOADED_JS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--script.js"


def test_download():
    html_original = read(ORIGINAL_HTML)
    html_expected = read(EXPECTED_HTML)
    img_expected = read(EXPECTED_IMG, binary=True)
    css_expected = read(EXPECTED_CSS, binary=True)
    js_expected = read(EXPECTED_JS, binary=True)
    txt_expected = read(EXPECTED_COURSES, binary=True)

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        mock.get(URL, text=html_original)
        mock.get(IMG_URL, content=img_expected)
        mock.get(CSS_URL, content=css_expected)
        mock.get(JS_URL, content=js_expected)
        mock.get(COURSES_URL, content=txt_expected)
        download(URL, tmpdir)

        actual_html = read(os.path.join(tmpdir, DOWNLOADED_HTML))
        actual_js = read(os.path.join(tmpdir, DOWNLOADED_JS), binary=True)
        actual_css = read(os.path.join(tmpdir, DOWNLOADED_CSS), binary=True)
        actual_img = read(os.path.join(tmpdir, DOWNLOADED_IMG), binary=True)

        assert actual_html == html_expected
        assert actual_img == img_expected
        assert actual_css == css_expected
        assert actual_js == js_expected


def test_get_resources():
    html_original = read(ORIGINAL_HTML)
    html_expected = read(EXPECTED_HTML)

    with requests_mock.Mocker() as mock:
        mock.get(URL, text=html_original)
        resources, html = get_resources(URL, 'page-loader-hexlet-repl-co-_files')
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


@pytest.mark.parametrize('url, expected_filename',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.html')])
def test_to_file(url, expected_filename):
    assert to_filename(url) == expected_filename


@pytest.mark.parametrize('url, expected_dir_name',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses_files')])
def test_to_dir(url, expected_dir_name):
    assert to_dir(url) == expected_dir_name


def test_directory_not_exist():
    try:
        download(URL, 'some_dir')
    except FileNotFoundError:
        print(f"Directory 'some_dir' doesn't exist")
