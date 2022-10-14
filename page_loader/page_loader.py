import os
import requests
import shutil
import logging.config
from bs4 import BeautifulSoup
from page_loader.name import to_filename, to_dir, to_resource_name
from page_loader.resources import get_resources
from urllib.parse import urljoin, urlparse
from page_loader.log import LOGGING_CONFIG
from page_loader.log import logger_info, logger_error


logging.config.dictConfig(LOGGING_CONFIG)


def download(url, filepath=os.getcwd()):
    """Download html and resources from url"""
    new_file_name = os.path.join(filepath, to_filename(url))
    dir_name = to_dir(url)
    dir_path = os.path.join(filepath, dir_name)
    response = requests.get(url)
    create_directory(dir_path)

    soup = BeautifulSoup(response.content, 'html.parser')
    resources, html = get_resources(url, dir_name)
    logger_info.info(f'Downloading resources')
    download_resources(url, dir_path, soup)
    logger_info.info(f'Downloading html from {url}')
    save(new_file_name, html)
    return new_file_name


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        logger_info.info(f'Create directory {dir_path}')
        os.mkdir(dir_path)
    else:
        logger_info.info(f'Directory {dir_path} has been already created.')


def download_resources(url, dir_name, soup):
    resources = []
    link_links = get_tags_links('link', 'href', soup)
    resources.extend(link_links)
    images = get_tags_links('img', 'src', soup)
    resources.extend(images)
    scripts = get_tags_links('script', 'src', soup)
    resources.extend(scripts)
    for resource in resources:
        link = urlparse(resource)
        if link.netloc == urlparse(url).netloc or link.netloc == '':
            download_links(url, resource, dir_name)


def get_tags_links(tag, attribute, soup):
    tags = [tag for tag in soup.findAll(tag)]
    tags_links = [
        each.get(attribute) for each in tags if each.get(attribute) is not None
    ]
    return tags_links


def download_links(url, link, dir_name):
    link_name = to_resource_name(url, link)
    filename = os.path.join(dir_name, link_name)
    src = urljoin(url, link)
    response = requests.get(src, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


def save(file_path, data, binary=False):
    if not binary:
        with open(file_path, 'w') as f:
            f.write(data)
    else:
        with open(file_path, 'wb') as f:
            f.write(data)
