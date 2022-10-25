import os
import requests
import shutil
import logging
from page_loader.url import to_filename, to_dir
from page_loader.resources import prepare_data
from urllib.parse import urljoin
from progress.bar import IncrementalBar


def download(url, dir_path=os.getcwd()):
    """Download html and resources from url"""
    if not os.path.exists(dir_path):
        logging.info(f"Directory {dir_path} doesn't exist."
                     f" Please, choose another directory.")
        raise FileNotFoundError
    new_file_name = os.path.join(dir_path, to_filename(url))
    dir_name = to_dir(url)
    new_dir_path = os.path.join(dir_path, dir_name)
    resources, html = prepare_data(url, dir_name)
    if not os.path.exists(new_dir_path):
        logging.info(f'Create directory {new_dir_path}')
        os.mkdir(new_dir_path)
    else:
        logging.info(f'Directory {new_dir_path} has been already created.')
    logging.info(f'Downloading resources from {url}')
    download_resources(resources, url, dir_path)
    logging.info(f'Downloading html from {url}')
    with open(new_file_name, 'w') as f:
        f.write(html)
    return new_file_name


def download_resources(resources, url, dir_name):
    if len(resources) == 0:
        logging.info(f'No resources for download from {url}')
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


def download_resource(url, resource, dir_name):
    filename = os.path.join(dir_name, resource[1])
    src = urljoin(url, resource[0])
    response = requests.get(src, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
