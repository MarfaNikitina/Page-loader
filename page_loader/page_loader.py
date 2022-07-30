import requests
import os
import re

def download(filepath, page_name):
    r = requests.get(page_name)
    pn_without_extension = os.path.splitext(page_name)[0]
    file_name_list = re.split('//|/|.', pn_without_extension)
    file_name = '-'.join(file_name_list) + '.html'
    new_fp = os.path.join(filepath, file_name)
    return new_fp
