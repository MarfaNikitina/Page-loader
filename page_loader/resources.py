from bs4 import BeautifulSoup
import requests
import os
from page_loader.url import to_resource_name
from urllib.parse import urlparse


def prepare_data(url, dir_name):
    response = requests.get(url)
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
