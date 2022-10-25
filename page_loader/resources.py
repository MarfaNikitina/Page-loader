from bs4 import BeautifulSoup
import requests
import os
from page_loader.url import to_resource_name
from urllib.parse import urlparse


def prepare_data(url, dir_name):
    response = requests.get(url)
    response.raise_for_status()
    data = BeautifulSoup(response.content, 'html.parser')
    tags = [
        ('img', 'src'),
        ('link', 'href'),
        ('script', 'src')
    ]
    resources = []
    for tag, attr in tags:
        tags_wanted = [
            (one, attr) for one in data.findAll(tag)
            if one.get(attr) is not None
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
