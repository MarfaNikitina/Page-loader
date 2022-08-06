import requests
# from bs4 import BeautifulSoup
import os
import re


def download(filepath, url, output=os.getcwd()):
    url_without_extension = os.path.splitext(url)[0]
    file_name_list = re.split('\//|\/|\.', url_without_extension)[1:]
    file_name = '-'.join(file_name_list) + '.html'
    new_fp = os.path.join(filepath, file_name)
    send_request = requests.get(url)
    with open(new_fp, 'w') as file:
        file.write(send_request.text)
    return new_fp


# with open("index.html") as fp:
    # soup = BeautifulSoup(fp, 'html.parser')