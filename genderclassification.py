import os
import sys
from scrape import get_remote_tgz_files, download_files

USAGE = """USAGE: %s <arg1> <arg2>."""
ARGCHECK = " \n"

SOURCE_URL = "http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit/"
DATA_DIR = "data"

if __name__ == '__main__':
    '''def usage():
        print USAGE % sys.argv[0]
        sys.exit(1)

    if len(sys.argv) != 3:
        usage()

    if not is_image(sys.argv[1]) or not is_image(sys.argv[2]):
        print ARGCHECK
        sys.exit(1)'''

    urls = get_remote_tgz_files(SOURCE_URL)
    download_extract_files(urls, DATA_DIR)

