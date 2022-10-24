from bs4 import BeautifulSoup
import logging
import requests
import os
from page_loader.url import to_resource_name
# from page_loader.log import logger_error, logger_info
from urllib.parse import urlparse


def get_data(url):
    try:
        response = requests.get(url)
        status = response.status_code
        logging.info(f'Page {url} exists. Getting response.'
                     f'Status_code {status}.'
                     f'Success.')
        response.raise_for_status()
    except requests.RequestException as error:
        logging.error(error)
        logging.info(f'Page {url} not found or status_code is not 200')
        raise Exception(error)
    return response


def prepare_data(response, url, dir_name):
    data = BeautifulSoup(response.content, 'html.parser')
    tags = ['img', 'link', 'script']
    resources = [tag for tag in data.findAll(tags)]
    tag_links = []
    for tag in resources:
        if tag.get('href') is not None:
            if is_desired_link(tag.get('href'), url):
                tag_links.append(tag.get('href'))
                resource_name = to_resource_name(url, tag['href'])
                tag['href'] = os.path.join(dir_name, resource_name)
        elif tag.get('src') is not None:
            if is_desired_link(tag.get('src'), url):
                tag_links.append(tag.get('src'))
                resource_name = to_resource_name(url, tag['src'])
                tag['src'] = os.path.join(dir_name, resource_name)
    return tag_links, data.prettify()


def is_desired_link(link, url):
    parsed = urlparse(link)
    return parsed.netloc == urlparse(url).netloc or parsed.netloc == ''

# result_links = [link for link in tags_links if is_desired_link(link, url)]
