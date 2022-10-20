import os
import re
from urllib.parse import urlparse


# def to_filename1(url):
#     url_without_extension = os.path.splitext(url)[0]
#     file_name_list = re.split(r'\//|\/|\.', url_without_extension)[1:]
#     file_name = '-'.join(file_name_list) + '.html'
#     return file_name


def replace_items(string):
    name_list = re.split(r'\/|\.', string)
    return '-'.join(name_list)


def to_filename(url):
    url_without_extension = os.path.splitext(url)[0]
    parsed_url = urlparse(url_without_extension)
    file_name = replace_items(f"{parsed_url.netloc}"
                              f"{parsed_url.path}") + '.html'
    return file_name


def to_dir(url):
    file_name = to_filename(url)
    dir_name = os.path.splitext(file_name)[0] + '_files'
    return dir_name


def to_resource_name(url, path):
    path_to_name = '-'.join(path.split('/'))
    # prefix = url.split('//')[1].split('/')[0]
    prefix = urlparse(url).netloc
    formatted_prefix = '-'.join(prefix.split('.'))
    return f"{formatted_prefix}{path_to_name}"
