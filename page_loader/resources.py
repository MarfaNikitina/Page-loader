from bs4 import BeautifulSoup
import logging.config
import requests
import os
from page_loader.log import LOGGING_CONFIG
from page_loader.name import to_resource_name
from page_loader.log import logger_error, logger_info
# from urllib.parse import urljoin, urlparse


logging.config.dictConfig(LOGGING_CONFIG)


def get_data(url):
    try:
        response = requests.get(url)
        status = response.status_code
        logger_info.info(f'Page {url} exists. Getting response. '
                         f'Status_code {status}. '
                         f'Success.')
    except requests.RequestException as error:
        logger_error.error(error)
        logger_info.info(f'Page {url} not found or status_code is not 200')
        raise Exception(error)
    return response


def get_resources(response, url, dir_name):
    data = BeautifulSoup(response.content, 'html.parser')
    tags = ['img', 'link', 'script']
    resources = [tag for tag in data.findAll(tags)]
    tags_links = []
    for each in resources:
        if each.get('href') is not None:
            tags_links.append(each.get('href'))
            resource_name = to_resource_name(url, each['href'])
            each['href'] = os.path.join(dir_name, resource_name)
        elif each.get('src') is not None:
            tags_links.append(each.get('src'))
            resource_name = to_resource_name(url, each['src'])
            each['src'] = os.path.join(dir_name, resource_name)
    return tags_links, data.prettify()
