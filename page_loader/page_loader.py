import os
import requests
import shutil
import logging.config
# from bs4 import BeautifulSoup
from page_loader.name import to_filename, to_dir, to_resource_name
from page_loader.resources import get_resources, get_data
from urllib.parse import urljoin, urlparse
from page_loader.log import LOGGING_CONFIG
from page_loader.log import logger_info, logger_error
from progress.bar import IncrementalBar


logging.config.dictConfig(LOGGING_CONFIG)


def download(url, filepath=os.getcwd()):
    """Download html and resources from url"""
    if not os.path.exists(filepath):
        logger_info.info(f"Directory {filepath} doesn't exist."
                         f" Please, choose another directory.")
        raise Exception
    new_file_name = os.path.join(filepath, to_filename(url))
    dir_name = to_dir(url)
    dir_path = os.path.join(filepath, dir_name)
    response = get_data(url)
    resources, html = get_resources(response, url, dir_name)
    create_directory(dir_path)
    logger_info.info(f'Downloading resources from {url}')
    download_resources(resources, url, dir_path)
    logger_info.info(f'Downloading html from {url}')
    save(new_file_name, html)
    return new_file_name


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        logger_info.info(f'Create directory {dir_path}')
        os.mkdir(dir_path)
    else:
        logger_info.info(f'Directory {dir_path} has been already created.')


def download_resources(resources, url, dir_name):
    if len(resources) == 0:
        logger_info.info(f'Downloading resources from {url}')
    with IncrementalBar(
            'Downloading:',
            max=len(resources),
            suffix='%(percent).1f%% - %(eta)ds'
    ) as bar:
        try:
            for resource in resources:
                bar.next()
                link = urlparse(resource)
                if link.netloc == urlparse(url).netloc or link.netloc == '':
                    download_links(url, resource, dir_name)
        except Exception as e:
            cause_info = (e.__class__, e, e.__traceback__)
            logger_info.info(str(e), exc_info=cause_info)
            logger_error.info(
                f"Page resource {resource} wasn't downloaded"
            )


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
