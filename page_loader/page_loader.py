import requests
import os
import re

def download(filepath, page_name, output):
    pn_without_extension = os.path.splitext(page_name)[0]
    file_name_list = re.split('\//|\/|\.', pn_without_extension)[1:]
    file_name = '-'.join(file_name_list) + '.html'
    new_fp = os.path.join(filepath, file_name)
    send_request = requests.get(page_name)
    with open(new_fp, 'w') as file:
        file.write(send_request.text)
    return new_fp
