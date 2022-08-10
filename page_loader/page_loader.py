import requests
from bs4 import BeautifulSoup
import os
from page_loader.name import to_file_name, to_dir, to_image_name


def download(url, filepath=os.getcwd()):
    new_fp = os.path.join(filepath, to_file_name(url))
    response = requests.get(url)
    write(new_fp, response.text)

    dir_name = os.path.join(filepath, to_dir(url))
    os.mkdir(dir_name)

    soup = BeautifulSoup(response.content, 'html.parser')
    image = soup.find('img')['src']
    image_name = to_image_name(url, image)
    write(os.path.join(dir_name, image_name), image)
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
