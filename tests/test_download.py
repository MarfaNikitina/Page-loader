import pytest
import os
from page_loader.url import to_filename
from page_loader.page_loader import download
import tempfile
import requests
import requests_mock
from page_loader.resources import prepare_data, is_desired_link
from tests import FIXTURES_PATH

URL = 'https://page-loader.hexlet.repl.co/'
MEDIA_FILES = [
    ('https://page-loader.hexlet.repl.co/assets/professions/nodejs.png',
        f"{FIXTURES_PATH}/fixture_img.png"),
    ('https://page-loader.hexlet.repl.co/assets/application.css',
     f"{FIXTURES_PATH}/fixture_css.css"),
    ('https://page-loader.hexlet.repl.co/script.js',
        f"{FIXTURES_PATH}/fixture_scripts.js"),
    ('https://page-loader.hexlet.repl.co/courses',
        f"{FIXTURES_PATH}/fixture_courses.txt")
]


@pytest.mark.parametrize('original, expected',
                         [('original_html.html', 'prettify_html.html')])
def test_download(original, expected):
    html_original = read(f"{FIXTURES_PATH}/{original}", 'r')
    html_expected = read(f"{FIXTURES_PATH}/{expected}", 'r')

    with requests_mock.Mocker() as mock, tempfile.TemporaryDirectory() as tmpdir:
        resources = MEDIA_FILES
        mock.get(URL, text=html_original)
        for url, path in resources:
            content = read(path, 'rb')
            mock.get(url, content=content)
        download(URL, tmpdir)
        actual_html = read(os.path.join(tmpdir, to_filename(URL)), 'r')
        assert actual_html == html_expected
        assert mock.call_count == 5


@pytest.mark.parametrize('original, expected',
                         [('original_html.html', 'prettify_html.html')])
def test_prepare_data(original, expected):
    html_original = read(f"{FIXTURES_PATH}/{original}", 'r')
    html_expected = read(f"{FIXTURES_PATH}/{expected}", 'r')

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


@pytest.mark.parametrize('mediafile_url, page_url',
                         [('/assets/professions/nodejs.png', 'https://page-loader.hexlet.repl.co/'),
                          ('/assets/application.css', 'https://page-loader.hexlet.repl.co/')]
                         )
def test_is_desired_link(mediafile_url, page_url):
    assert is_desired_link(mediafile_url, page_url)
