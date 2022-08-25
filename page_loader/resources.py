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


# def download_resources(url, dir_name):
#     resources, html = get_resources(url, dir_name)
#     teg_attr_dictionary = {
#         'img': 'src',
#         'script': 'src',
#         'link': 'href'
#     }
#     links = []
#     for each in resources:
#         
#         
#         
#     link_links = get_tags_links('link', 'href', soup)
#     resources.extend(link_links)
#     images = get_tags_links('img', 'src', soup)
#     resources.extend(images)
#     scripts = get_tags_links('script', 'src', soup)
#     resources.extend(scripts)
#     for resource in resources:
#         link = urlparse(resource)
#         if link.netloc == urlparse(url).netloc or link.netloc == '':
#             download_links(url, resource, dir_name)
# 
# 
# def get_tags_links(tag, attribute, soup):
#     tags = [tag for tag in soup.findAll(tag)]
#     tags_links = [
#         each.get(attribute) for each in tags if each.get(attribute) is not None
#     ]
#     return tags_links
# 
# 
# def download_links(url, link, dir_name):
#     link_name = to_resource_name(url, link)
#     filename = os.path.join(dir_name, link_name)
#     src = urljoin(url, link)
#     response = requests.get(src, stream=True)
#     with open(filename, 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
