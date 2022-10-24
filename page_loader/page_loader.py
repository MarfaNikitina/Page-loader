import os
import requests
import shutil
# import logging.config
import logging
from page_loader.url import to_filename, to_dir, to_resource_name
from page_loader.resources import prepare_data, get_data
from urllib.parse import urljoin
# from page_loader.log import LOGGING_CONFIG
# from page_loader.log import logger_info, logger_error
from progress.bar import IncrementalBar


def download(url, filepath=os.getcwd()):
    """Download html and resources from url"""
    if not os.path.exists(filepath):
        logging.info(f"Directory {filepath} doesn't exist."
                     f" Please, choose another directory.")
        raise FileNotFoundError
    new_file_name = os.path.join(filepath, to_filename(url))
    dir_name = to_dir(url)
    dir_path = os.path.join(filepath, dir_name)
    response = get_data(url)
    resources, html = prepare_data(response, url, dir_name)
    create_directory(dir_path)
    logging.info(f'Downloading resources from {url}')
    download_resources(resources, url, dir_path)
    logging.info(f'Downloading html from {url}')
    with open(new_file_name, 'w') as f:
        f.write(html)
    return new_file_name


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        logging.info(f'Create directory {dir_path}')
        os.mkdir(dir_path)
    else:
        logging.info(f'Directory {dir_path} has been already created.')


def download_resources(resources, url, dir_name):
    if len(resources) == 0:
        logging.info(f'Downloading resources from {url}')
    with IncrementalBar(
            'Downloading:',
            max=len(resources),
            suffix='%(percent).1f%% - %(eta)ds'
    ) as bar:
        try:
            for resource in resources:
                bar.next()
                download_resource(url, resource, dir_name)
        except Exception as e:
            cause_info = (e.__class__, e, e.__traceback__)
            logging.info(str(e), exc_info=cause_info)
            logging.error(
                f"Page resource {resource} wasn't downloaded"
            )


def download_resource(url, link, dir_name):
    link_name = to_resource_name(url, link)
    filename = os.path.join(dir_name, link_name)
    src = urljoin(url, link)
    response = requests.get(src, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
