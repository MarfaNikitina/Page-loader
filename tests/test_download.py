import pytest
import os
from page_loader.name import to_filename, to_dir
from page_loader.page_loader import download
import tempfile
import requests_mock


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


# URL1 = 'https://ru.hexlet.io/courses'
URL = 'https://page-loader.hexlet.repl.co'
IMG_URL = 'https://page-loader.hexlet.repl.co/assets/professions/nodejs.png'
CSS_URL = 'https://page-loader.hexlet.repl.co/assets/application.css'
JS_URL = 'https://page-loader.hexlet.repl.co/script.js'


EXPECTED_HTML = f"{FIXTURES_PATH}/prettify_html.html"
EXPECTED_IMG = f"{FIXTURES_PATH}/img.png"
EXPECTED_CSS = f"{FIXTURES_PATH}/fixture_css.css"
EXPECTED_JS = f"{FIXTURES_PATH}/fixture_scripts.js"


DOWNLOADED_HTML = 'page-loader-hexlet-repl-co-.html'
DOWNLOADED_IMG = 'page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--assets-professions-nodejs.png'
DOWNLOADED_CSS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--assets-application.css"
DOWNLOADED_JS = "page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co--script.js"


@pytest.mark.parametrize('url, expected_result',
                         [('https://page-loader.hexlet.repl.co/', 'page-loader-hexlet-repl-co-.html')])
def test_download(url, expected_result):
    html_expected = read(EXPECTED_HTML)
    img_expected = read(EXPECTED_IMG, binary=True)
    css_expected = read(EXPECTED_CSS, binary=True)
    js_expected = read(EXPECTED_JS, binary=True)

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        mock.get(URL, text=html_expected)
        mock.get(IMG_URL, content=img_expected)
        mock.get(CSS_URL, content=css_expected)
        mock.get(JS_URL, content=js_expected)
        download(URL, tmpdir)

        actual_html = read(os.path.join(tmpdir, DOWNLOADED_HTML))
        actual_js = read(os.path.join(tmpdir, DOWNLOADED_JS), binary=True)
        actual_css = read(os.path.join(tmpdir, DOWNLOADED_CSS), binary=True)
        actual_img = read(os.path.join(tmpdir, DOWNLOADED_IMG), binary=True)

        assert actual_html == html_expected
        assert actual_img == img_expected
        assert actual_css == css_expected
        assert actual_js == js_expected


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