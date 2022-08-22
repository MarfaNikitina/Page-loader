import os
import re
from urllib.parse import urlparse


# def replace_items(url):
#     result = re.sub(r"[^0-9a-zA-Z]", "-", f"{url}")
#     return result


# def to_file_name1(url):
#     parsed_url = urlparse(url)
def to_filename(url):
    url_without_extension = os.path.splitext(url)[0]
    # url_without_schema = url_without_extension.split('//')[1:]
    file_name_list = re.split('\//|\/|\.', url_without_extension)[1:]
    file_name = '-'.join(file_name_list) + '.html'
    # file_name = replace_items(url_without_schema) + '.html'
    return file_name


def to_dir(url):
    file_name = to_filename(url)
    dir_name = os.path.splitext(file_name)[0] + '_files'
    return dir_name


def to_resource_name(url, path):
    path_to_name = '-'.join(path.split('/'))
    prefix = url.split('//')[1].split('/')[0]
    formatted_prefix = '-'.join(prefix.split('.'))
    return f"{formatted_prefix}-{path_to_name}"
