import os
import re


def to_filename(url):
    url_without_extension = os.path.splitext(url)[0]
    file_name_list = re.split('\//|\/|\.', url_without_extension)[1:]
    file_name = '-'.join(file_name_list) + '.html'
    return file_name


def to_dir(url):
    file_name = to_filename(url)
    dir_name = os.path.splitext(file_name)[0] + '_files'
    return dir_name


def to_image_name(url, path):
    path_to_name = '-'.join(path.split('/'))
    prefix = url.split('//')[1].split('/')[0]
    formatted_prefix = '-'.join(prefix.split('.'))
    return f"{formatted_prefix}-{path_to_name}"