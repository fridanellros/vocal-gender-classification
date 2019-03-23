import os
import sys
from scrape import get_remote_tgz_files, download_extract_files
from parse import paths, parse_readme
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

    data_folder = Path(DATA_DIR)

    ## --- SCRAPE FOR FILES ---
    #urls = get_remote_tgz_files(SOURCE_URL)
    #download_extract_files(urls, data_folder)

    conn = sqlite3.connect('example.db')
    db = conn.cursor()
    db.execute('''DROP TABLE IF EXISTS features''')
    db.execute('''CREATE TABLE features
             (file text unique, path text, female integer, 
                age text, language text, dialect text)''')

    samples = os.listdir(data_folder)
    for sample in samples:
        (wav_folder, readme_path) = paths(data_folder, sample)
        meta = parse_readme(readme_path)

        wavs = os.listdir(wav_folder)
        for wav in wavs:
            db.execute('''INSERT INTO features VALUES
             (?,?,?,?,?,?)''', 
                (wav[:-4], 
                str(wav_folder), 
                meta['Gender'] == 'Female', 
                meta['Age Range'], 
                meta['Language'], 
                meta['Pronunciation dialect']))

        db.execute('''SELECT file, female, age, language, dialect FROM features''')
        print(db.fetchall())
        break

        
    conn.commit()
    conn.close()

