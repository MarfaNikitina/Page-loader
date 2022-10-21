import pytest
from urllib.parse import urlparse
import os
from page_loader.name import to_filename, to_dir, to_resource_name
from page_loader.page_loader import download
import tempfile
import requests
import requests_mock
from page_loader.resources import get_resources

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


TEST_DATA = {
    'HTML': [
        'https://page-loader.hexlet.repl.co/',
        f"{FIXTURES_PATH}/original_html.html",
        f"{FIXTURES_PATH}/prettify_html.html"
    ],
    'IMG': [
        'https://page-loader.hexlet.repl.co/assets/professions/nodejs.png',
        f"{FIXTURES_PATH}/fixture_img.png"
    ],
    'CSS': [
        'https://page-loader.hexlet.repl.co/assets/application.css',
        f"{FIXTURES_PATH}/fixture_css.css"
    ],
    'JS': [
        'https://page-loader.hexlet.repl.co/script.js',
        f"{FIXTURES_PATH}/fixture_scripts.js"
    ],
    'COURSES': [
        'https://page-loader.hexlet.repl.co/courses',
        f"{FIXTURES_PATH}/fixture_courses.txt"
    ]
}

# DOWNLOADED_HTML = 'page-loader-hexlet-repl-co-.html'
# DOWNLOADED_TXT = 'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-courses.html'
# DOWNLOADED_IMG = 'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-professions-nodejs.png'
# DOWNLOADED_CSS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-application.css"
# DOWNLOADED_JS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-script.js"

URL = TEST_DATA['HTML'][0]
DOWNLOADED_HTML = to_filename(URL)
DOWNLOADED_TXT = os.path.join(to_dir(URL), to_resource_name(URL, urlparse(TEST_DATA['COURSES'][0]).path))
DOWNLOADED_IMG = os.path.join(to_dir(URL), to_resource_name(URL, urlparse(TEST_DATA['IMG'][0]).path))
DOWNLOADED_CSS = os.path.join(to_dir(URL), to_resource_name(URL, urlparse(TEST_DATA['CSS'][0]).path))
DOWNLOADED_JS = os.path.join(to_dir(URL), to_resource_name(URL, urlparse(TEST_DATA['JS'][0]).path))


def test_download():
    html_original = read(TEST_DATA['HTML'][1])
    html_expected = read(TEST_DATA['HTML'][2])
    img_expected = read(TEST_DATA['IMG'][1], binary=True)
    css_expected = read(TEST_DATA['CSS'][1], binary=True)
    js_expected = read(TEST_DATA['JS'][1], binary=True)
    txt_expected = read(TEST_DATA['COURSES'][1], binary=True)

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        mock.get(TEST_DATA['HTML'][0], text=html_original)
        mock.get(TEST_DATA['IMG'][0], content=img_expected)
        mock.get(TEST_DATA['CSS'][0], content=css_expected)
        mock.get(TEST_DATA['JS'][0], content=js_expected)
        mock.get(TEST_DATA['COURSES'][0], content=txt_expected)
        download(TEST_DATA['HTML'][0], tmpdir)

        actual_html = read(os.path.join(tmpdir, DOWNLOADED_HTML))
        actual_js = read(os.path.join(tmpdir, DOWNLOADED_JS), binary=True)
        actual_css = read(os.path.join(tmpdir, DOWNLOADED_CSS), binary=True)
        actual_img = read(os.path.join(tmpdir, DOWNLOADED_IMG), binary=True)

        assert actual_html == html_expected
        assert actual_img == img_expected
        assert actual_css == css_expected
        assert actual_js == js_expected


def test_get_resources():
    html_original = read(TEST_DATA['HTML'][1])
    html_expected = read(TEST_DATA['HTML'][2])

    with requests_mock.Mocker() as mock:
        mock.get(TEST_DATA['HTML'][0], text=html_original)
        response = requests.get(TEST_DATA['HTML'][0])
        resources, html = get_resources(response, TEST_DATA['HTML'][0], 'page-loader-hexlet-repl-co-_files')
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
        download(TEST_DATA['HTML'][0], 'some_dir')
    except FileNotFoundError:
        print("Directory 'some_dir' doesn't exist")


def test_false_response():
    with pytest.raises(Exception) as e:
        download('https://notexist.com')

        assert str(e.value) == requests.RequestException
