import os
import sys
import requests
import tarfile
from bs4 import BeautifulSoup

def get_remote_tgz_files(base_url):
    response = requests.get(base_url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    urls = []
    for link in content.findAll('a'):
        name = link.get('href')
        if name.endswith('.tgz'):
            urls.append((name[:-4], base_url + link.get('href')))

    return urls


def download_extract_files(urls, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    subdirs = os.listdir(dest_dir)
    for u in urls:
        if u[0] in subdirs:
            continue
        response = requests.get(u[1], stream=True)
        tar = tarfile.open(mode='r|gz', fileobj=response.raw)
        tar.extractall(dest_dir)
        response.close()
