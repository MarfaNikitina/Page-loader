import requests
from bs4 import BeautifulSoup
import os
from page_loader.name import to_filename, to_dir, to_resource_name
import shutil
from urllib.parse import urljoin, urlparse
import time


def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_filename(url))
    response = requests.get(url)
    dir_name = to_dir(url)
    dir_path = os.path.join(filepath, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    soup = BeautifulSoup(response.content, 'html.parser')
    download_resources(url, dir_path, soup)
    resources = []
    images = [img for img in soup.findAll('img')]
    links = [link for link in soup.findAll('link')]
    scripts = [
        script for script in soup.findAll('script') if script.get('src') is not None
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
    write(new_fp, soup.prettify())
    return new_fp


def download_resources(url, dir_name, soup):
    resources = []
    link_links = get_tags_links('link', 'href', soup)
    resources.extend(link_links)
    images = get_tags_links('img', 'src', soup)
    resources.extend(images)
    scripts = get_tags_links('script', 'src', soup)
    resources.extend(scripts)
    for resource in resources:
        link = urlparse(resource)
        if link.netloc == urlparse(url).netloc or link.netloc == '':
            download_links(url, resource, dir_name)


def get_tags_links(tag, attribute, soup):
    tags = [tag for tag in soup.findAll(tag)]
    tags_links = [
        each.get(attribute) for each in tags if each.get(attribute) is not None
    ]
    return tags_links


def download_links(url, link, dir_name):
    link_name = to_resource_name(url, link)
    filename = os.path.join(dir_name, link_name)
    src = urljoin(url, link)
    response = requests.get(src, stream=True)
    time.sleep(1)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        # except:
        #     print('  An error occured. Continuing.')
    print('Done.')


def write(file_path, data, binary=False):
    if not binary:
        with open(file_path, 'w') as f:
            f.write(data)
    else:
        with open(file_path, 'wb') as f:
            f.write(data)


    # for each in list_of_links:
    #     try:
    #         print(each)
    #         link_name = to_resource_name(url, each)
    #         filename = os.path.join(dir_name, link_name)
    #         src = urljoin(url, each)
    #         response = requests.get(src, stream=True)
    #         time.sleep(1)
    #         with open(filename, 'wb') as out_file:
    #             shutil.copyfileobj(response.raw, out_file)
    #     except:
    #         print('  An error occured. Continuing.')
    # print('Done.')