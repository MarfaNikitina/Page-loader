import requests
from bs4 import BeautifulSoup
import os
from page_loader.name import to_file_name, to_dir, to_image_name
import shutil
from urllib.parse import urljoin
import time


def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_file_name(url))
    response = requests.get(url)
    write(new_fp, response.text)
    dir_name = os.path.join(filepath, to_dir(url))
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    soup = BeautifulSoup(response.content, 'html.parser')
    images = [img for img in soup.findAll('img')]
    print(str(len(images)) + " images found.")
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    for each in image_links:
        try:
            image_name = to_image_name(url, each)
            filename = os.path.join(dir_name, image_name)
            src = urljoin(url, each)
            print('Getting: ' + filename)
            response = requests.get(src, stream=True)
            time.sleep(1)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print('  An error occured. Continuing.')
    print('Done.')
    return new_fp



def write(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)


# def _right(file_path):
#     data = read(file_path)
# 
#     write(
#         file_path,
#         BeautifulSoup(data, 'html.parser').prettify()
#     )
