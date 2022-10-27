import os
import re
from urllib.parse import urlparse


# def to_filename(url):
#     url_without_extension = os.path.splitext(url)[0]
#     parsed_url = urlparse(url_without_extension)
#     path_string = f"{parsed_url.netloc}{parsed_url.path}"
#     path_to_replace = re.split(r'\/|\.', path_string)
#     file_name = '-'.join(path_to_replace) + '.html'
#     return file_name


def to_filename(url, resource_path=''):
    if resource_path == '':
        resource_path = url
    # url_without_extension = os.path.splitext(url)[0]
    parsed_url = urlparse(url)
    desired_resource_path = urlparse(resource_path).path.split('/')
    desired_netloc = re.split(r'\/|\.', parsed_url.netloc)
    file_name = '-'.join(desired_netloc) + '-'.join(desired_resource_path)
    if os.path.splitext(resource_path)[1] == '':
        file_name += '.html'
    return file_name


# def to_resource_name(url, resource_path):
#     desired_path = urlparse(resource_path).path
#     path_to_name = '-'.join(desired_path.split('/'))
#     if os.path.splitext(resource_path)[1] == '':
#         path_to_name += '.html'
#     prefix = urlparse(url).netloc
#     formatted_prefix = '-'.join(prefix.split('.'))
#     return f"{formatted_prefix}{path_to_name}"


def to_dir(url):
    file_name = to_filename(url)
    filepath, _ = os.path.splitext(file_name)
    dir_name = filepath + '_files'
    return dir_name
