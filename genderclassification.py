import os
import sys
from scrape import get_remote_tgz_files, download_extract_files
from pathlib import Path
import sqlite3

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

    #urls = get_remote_tgz_files(SOURCE_URL)
    #download_extract_files(urls, DATA_DIR)

    conn = sqlite3.connect('example.db')
    db = conn.cursor()
    db.execute('''DROP TABLE IF EXISTS features''')
    db.execute('''CREATE TABLE features
             (file text unique, path text, female integer, rate integer, 
                format integer, age text, language text, dialect text)''')

    samples = os.listdir(DATA_DIR)
    for sample in samples:
        data_folder = Path(DATA_DIR)
        wav_folder = data_folder / sample / "wav"
        readme = data_folder / sample / "etc" / "README"

        wavs = os.listdir(wav_folder)
        for wav in wavs:
            db.execute('''INSERT INTO features VALUES
             (?,?,?,?,?,?,?,?)''', (str(wav), str(wav_folder), 0, 0, 0, '', '', ''))

        print(os.listdir(wav_folder))
        print(readme)
        a = db.execute('''SELECT * FROM features''')
        break

        
    conn.commit()
    conn.close()

