import requests
from bs4 import BeautifulSoup
import os
from page_loader.name import to_filename, to_dir, to_image_name
import shutil
from urllib.parse import urljoin
import time


def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_filename(url))
    response = requests.get(url)
    dir_name = os.path.join(filepath, to_dir(url))
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    soup = BeautifulSoup(response.content, 'html.parser')
    download_resources(url, dir_name, soup)
    images = [img for img in soup.findAll('img')]
    links = [link for link in soup.findAll('link')]
    for lnk in links:
        image_name = to_image_name(url, lnk['href'])
        lnk['href'] = os.path.join(dir_name, image_name)
    scripts = [script for script in soup.findAll('script') if script.get('src') is not None]
    images.extend(scripts)
    for img in images:
        image_name = to_image_name(url, img['src'])
        img['src'] = os.path.join(dir_name, image_name)
    write(new_fp, soup.prettify())
    return new_fp


def download_resources(url, dir_name, soup):
    resources = []
    links = [link for link in soup.findAll('link')]
    link_links = [each.get('href') for each in links]
    download_links(url, link_links, dir_name)
    images = [img for img in soup.findAll('img')]
    resources.extend(images)
    scripts = [script for script in soup.findAll('script') if script.get('src') is not None]
    resources.extend(scripts)
    resources_links = [each.get('src') for each in resources]
    download_links(url, resources_links, dir_name)
    print('Done.')


def download_links(url, list_of_links, dir_name):
    for each in list_of_links:
        try:
            print(each)
            link_name = to_image_name(url, each)
            filename = os.path.join(dir_name, link_name)
            attr = urljoin(url, each)
            response = requests.get(attr, stream=True)
            time.sleep(1)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print('  An error occured. Continuing.')
    print('Done.')


def write(file_path, data, binary=False):
    if not binary:
        with open(file_path, 'w') as f:
            f.write(data)
    else:
        with open(file_path, 'wb') as f:
            f.write(data)


# def download_img(url, dir_name, soup):
#     images = [img for img in soup.findAll('img')]
#     print(str(len(images)) + " images found.")
#     print('Downloading images to current working directory.')
#     image_links = [each.get('src') for each in images]
#     for each in image_links:
#         try:
#             print(each)
#             image_name = to_image_name(url, each)
#             filename = os.path.join(dir_name, image_name)
#             src = urljoin(url, each)
#             print('Getting: ' + filename)
#             response = requests.get(src, stream=True)
#             time.sleep(1)
#             # write(response.raw, filename, binary=True)
#             with open(filename, 'wb') as out_file:
#                 shutil.copyfileobj(response.raw, out_file)
#         except:
#             print('  An error occured. Continuing.')
#     print('Done.')

    # for each in resources_links:
    #     try:
    #         print(each)
    #         link_name = to_image_name(url, each)
    #         filename = os.path.join(dir_name, link_name)
    #         src = urljoin(url, each)
    #         # print('Getting: ' + filename)
    #         response = requests.get(src, stream=True)
    #         time.sleep(1)
    #         with open(filename, 'wb') as out_file:
    #             shutil.copyfileobj(response.raw, out_file)
    #     except:
    #         print('  An error occured. Continuing.')

    # for each in link_links:
    #     try:
    #         print(each)
    #         link_name = to_image_name(url, each)
    #         filename = os.path.join(dir_name, link_name)
    #         href = urljoin(url, each)
    #         response = requests.get(href, stream=True)
    #         time.sleep(1)
    #         with open(filename, 'wb') as out_file:
    #             shutil.copyfileobj(response.raw, out_file)
    #     except:
    #         print('  An error occured. Continuing.')
    # print('Done.')
