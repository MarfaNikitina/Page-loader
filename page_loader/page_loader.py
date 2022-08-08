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



def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_file(url))
    response = requests.get(url)
    with open(new_fp, 'w') as file:
        file.write(response.text)
    dir_name = os.path.join(filepath, to_dir(url))
    return new_fp


# def read(file_path):
#     with open(file_path, 'r') as f:
#         result = f.read()
#     return result
# 
# 
# def write(file_path, data):
#     with open(file_path, 'w') as f:
#         f.write(data)
# 
# 
# def _right(file_path):
#     data = read(file_path)
# 
#     write(
#         file_path,
#         BeautifulSoup(data, 'html.parser').prettify()
#     )

# with open("index.html") as fp:
    # soup = BeautifulSoup(fp, 'html.parser')
   # images = soup.find_all('img')
   
   
# r = requests.get("xxx")
# soup = BeautifulSoup(r.content)
# for link in soup.select("img[src^=http]"):
#         lnk = link["src"]
#         with open(basename(lnk)," wb") as f:
#             f.write(requests.get(lnk).content)