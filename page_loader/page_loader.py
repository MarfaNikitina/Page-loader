import requests
from bs4 import BeautifulSoup
import os
import re


def to_file(url):
    url_without_extension = os.path.splitext(url)[0]
    file_name_list = re.split('\//|\/|\.', url_without_extension)[1:]
    file_name = '-'.join(file_name_list) + '.html'
    return file_name


def to_dir(url):
    file_name = to_file(url)
    dir_name = os.path.splitext(file_name)[0] + '_files'
    return dir_name


def to_image_name(url, path):
    path_to_name = '-'.join(path.split('/'))
    prefix = url.split('//')[1].split('/')[0]
    formatted_prefix = '-'.join(prefix.split('.'))
    return f"{formatted_prefix}-{path_to_name}"


def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_file(url))
    response = requests.get(url)
    write(new_fp, response.text)

    dir_name = os.path.join(filepath, to_dir(url))
    os.mkdir(dir_name)

    soup = BeautifulSoup(response.content, 'html.parser')
    image = soup.find('img')['src']
    image_name = to_image_name(url, image)
    write(os.path.join(dir_name, image_name), image)
    # print(image)
    # print(image_name)
    return new_fp


# def read(file_path):
#     with open(file_path, 'r') as f:
#         result = f.read()
#     return result
# 
# 
def write(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

# 
# 
# def _right(file_path):
#     data = read(file_path)
# 
#     write(
#         file_path,
#         BeautifulSoup(data, 'html.parser').prettify()
#     )

   
   
# r = requests.get("xxx")
# soup = BeautifulSoup(r.content)
# for link in soup.select("img[src^=http]"):
#         lnk = link["src"]
#         with open(basename(lnk)," wb") as f:
#             f.write(requests.get(lnk).content)
