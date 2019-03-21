import os
import sys
from bs4 import BeautifulSoup
import requests
import tarfile

USAGE = """USAGE: %s <path_to_image> <path_to_image> 
    Determines whether two images are similar,
    by comparing image hash distance and hue color properties."""
ARGCHECK = "Requires a .png, .jpg, .jpeg, .bmp, or .gif file \n"

SOURCE_URL = "http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/"

SOURCE_DIR = "data"

if __name__ == '__main__':
    '''def usage():
        print USAGE % sys.argv[0]
        sys.exit(1)

    if len(sys.argv) != 3:
        usage()

    if not is_image(sys.argv[1]) or not is_image(sys.argv[2]):
        print ARGCHECK
        sys.exit(1)'''

    response = requests.get(SOURCE_URL, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    urls = []
    names = []
    for link in content.findAll('a'):
        name = link.get('href')
        if name.endswith('.tgz'):
            urls.append(SOURCE_URL + link.get('href'))
            names.append(name[:-4])

    if not os.path.exists(SOURCE_DIR):
        os.mkdir(SOURCE_DIR)

    subdirs = os.listdir(SOURCE_DIR)
    print(subdirs)
    
    for i in range(0,len(urls)):
        print(names[i])
        if names[i] in subdirs:
            continue
        response = requests.get(urls[i], stream=True)
        tar = tarfile.open(mode='r|gz', fileobj=response.raw)
        tar.extractall(SOURCE_DIR)
        response.close()
        print("DONE")  
  	

