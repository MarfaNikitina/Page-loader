import os
import re
from urllib.parse import urlparse


def to_filename(url, resource_path=''):
    if resource_path == '':
        resource_path = url
    parsed_url = urlparse(url)
    desired_resource_path = urlparse(resource_path).path.split('/')
    desired_netloc = re.split(r'\/|\.', parsed_url.netloc)
    file_name = '-'.join(desired_netloc) + '-'.join(desired_resource_path)
    if os.path.splitext(resource_path)[1] == '':
        file_name += '.html'
    return file_name


def to_dir(url):
    file_name = to_filename(url)
    filepath, _ = os.path.splitext(file_name)
    dir_name = filepath + '_files'
    return dir_name
