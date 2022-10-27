from bs4 import BeautifulSoup
import logging
import requests
import os
from page_loader.url import to_filename, to_dir
from urllib.parse import urlparse


RESOURCE_TAGS = [
    ('img', 'src'),
    ('link', 'href'),
    ('script', 'src')
]


def prepare_data(url, dir_path=os.getcwd()):
    response = requests.get(url)
    response.raise_for_status()
    page = BeautifulSoup(response.content, 'html.parser')
    dir_name = to_dir(url)
    media_resources_path = os.path.join(dir_path, dir_name)
    if not os.path.exists(media_resources_path):
        logging.info(f'Create directory {media_resources_path}')
        os.mkdir(media_resources_path)
    else:
        logging.info(f'Directory {media_resources_path}'
                     f' has been already created.')
    resources = []
    for tag, attribute in RESOURCE_TAGS:
        tags_wanted = [
            (tag_name, attribute) for tag_name in page.findAll(tag)
            if tag_name.get(attribute) is not None
        ]
        resources.extend(tags_wanted)
    resource_pair = []
    for tag, attribute in resources:
        if is_desired_link(tag.get(attribute), url):
            tag_link = tag.get(attribute)
            resource_name = to_filename(url, tag[attribute])
            tag[attribute] = os.path.join(dir_name, resource_name)
            resource_pair.append((tag_link, tag[attribute]))
    return resource_pair, page.prettify()


def is_desired_link(link, url):
    parsed = urlparse(link)
    return parsed.netloc == urlparse(url).netloc or parsed.netloc == ''
