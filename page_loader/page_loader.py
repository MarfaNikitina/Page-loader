import os
import requests
import logging
from page_loader.url import to_filename
from page_loader.resources import prepare_data
from urllib.parse import urljoin
from progress.bar import IncrementalBar


def download(url, dir_path=os.getcwd()):
    """Download html and resources from url"""
    if not os.path.exists(dir_path):
        logging.info(f"Directory {dir_path} doesn't exist."
                     f" Please, choose another directory.")
        raise FileNotFoundError
    path_to_html = os.path.join(dir_path, to_filename(url))
    resources, html = prepare_data(url, dir_path)
    download_resources(resources, url, dir_path)
    logging.info(f'Downloading html from {url}')
    with open(path_to_html, 'w') as f:
        f.write(html)
    return path_to_html


def download_resources(resources, url, dir_path):
    if len(resources) == 0:
        logging.info(f'No resources to download from {url}')
        return
    logging.info(f'Downloading resources from {url}')
    with IncrementalBar(
            'Downloading:',
            max=len(resources),
            suffix='%(percent).1f%% - %(eta)ds'
    ) as bar:
        try:
            for resource in resources:
                bar.next()
                resource_url, resource_path = resource
                download_resource(url, resource_url, resource_path, dir_path)
        except Exception as e:
            cause_info = (e.__class__, e, e.__traceback__)
            logging.info(str(e), exc_info=cause_info)
            logging.error(
                f"Page resource {resource} wasn't downloaded"
            )


def download_resource(url, resource_url, resource_path, dir_path):
    fullpath = os.path.join(dir_path, resource_path)
    src = urljoin(url, resource_url)
    response = requests.get(src, stream=True)
    with open(fullpath, 'wb') as out_file:
        out_file.write(response.content)
