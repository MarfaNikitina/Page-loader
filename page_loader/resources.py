from bs4 import BeautifulSoup
import requests
import os
from page_loader.name import to_resource_name


def get_resources(url, dir_name):
    response = requests.get(url)
    data = BeautifulSoup(response.content, 'html.parser')
    # tegs = ['img', 'link', 'script']
    resources = []
    images = [img for img in data.findAll('img')]
    links = [link for link in data.findAll('link')]
    scripts = [
        script for script in data.findAll('script') if script.get('src') is not None
    ]
    resources.extend(images)
    resources.extend(links)
    resources.extend(scripts)
    for each in resources:
        if each.get('href') is not None:
            resource_name = to_resource_name(url, each['href'])
            each['href'] = os.path.join(dir_name, resource_name)
        else:
            resource_name = to_resource_name(url, each['src'])
            each['src'] = os.path.join(dir_name, resource_name)
    return resources, data.prettify()
