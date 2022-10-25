from bs4 import BeautifulSoup
import logging
import requests
import os
from page_loader.url import to_resource_name, to_dir
from urllib.parse import urlparse


def prepare_data(url, dir_path=os.getcwd()):
    response = requests.get(url)
    response.raise_for_status()
    data = BeautifulSoup(response.content, 'html.parser')
    dir_name = to_dir(url)
    new_dir_path = os.path.join(dir_path, dir_name)
    if not os.path.exists(new_dir_path):
        logging.info(f'Create directory {new_dir_path}')
        os.mkdir(new_dir_path)
    else:
        logging.info(f'Directory {new_dir_path} has been already created.')
    tags = [
        ('img', 'src'),
        ('link', 'href'),
        ('script', 'src')
    ]
    resources = []
    for tag, attribute in tags:
        tags_wanted = [
            (tag_name, attribute) for tag_name in data.findAll(tag)
            if tag_name.get(attribute) is not None
        ]
        resources.extend(tags_wanted)
    resource_pair = []
    for tag, attribute in resources:
        if is_desired_link(tag.get(attribute), url):
            tag_link = tag.get(attribute)
            resource_name = to_resource_name(url, tag[attribute])
            tag[attribute] = os.path.join(dir_name, resource_name)
            resource_pair.append((tag_link, tag[attribute]))
    return resource_pair, data.prettify()


def is_desired_link(link, url):
    parsed = urlparse(link)
    return parsed.netloc == urlparse(url).netloc or parsed.netloc == ''
