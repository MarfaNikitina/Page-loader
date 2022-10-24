import pytest
from page_loader.url import to_filename, to_dir, to_resource_name
from page_loader import download


URL = 'https://page-loader.hexlet.repl.co/'


@pytest.mark.parametrize('url, expected_filename',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses.html')])
def test_to_file(url, expected_filename):
    assert to_filename(url) == expected_filename


@pytest.mark.parametrize('url, expected_dir_name',
                         [('https://ru.hexlet.io/courses', 'ru-hexlet-io-courses_files')])
def test_to_dir(url, expected_dir_name):
    assert to_dir(url) == expected_dir_name


@pytest.mark.parametrize('url, resource_path, expected_name',
                         [('https://page-loader.hexlet.repl.co/',
                           '/assets/professions/nodejs.png',
                           'page-loader-hexlet-repl-co-assets-professions-nodejs.png'
                           ),
                          ('https://page-loader.hexlet.repl.co/',
                           'https://page-loader.hexlet.repl.co/assets/application.css',
                           'page-loader-hexlet-repl-co-assets-application.css',
                           )
                          ])
def test_to_resource_name(url, resource_path, expected_name):
    assert to_resource_name(url, resource_path) == expected_name


def test_directory_not_exist():
    try:
        download(URL, 'some_dir')
    except FileNotFoundError:
        print("Directory 'some_dir' doesn't exist")
