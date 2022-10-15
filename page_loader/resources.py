from bs4 import BeautifulSoup
import requests
import os
from page_loader.name import to_resource_name
# from urllib.parse import urljoin, urlparse


def get_resources(url, dir_name):
    response = requests.get(url)
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
