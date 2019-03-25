import os
from pathlib import Path

def paths(folder, sample):    
    wav_folder = None
    readme_path = None
    
    for root, dirs, files in os.walk(folder / sample):
        for f in files:
            if f.lower().endswith("readme"):
                readme_path = Path(root) / f
                break
        for d in dirs:
            if d.lower().endswith("wav"):
                wav_folder = Path(root) / d
    
    return(wav_folder, readme_path)

def parse_readme(path) -> dict:
    def sanitize(s):
        import re
        return re.sub('[\W]+', '', s).lower()

    r = open(path, "r")
    lines = r.readlines()
    r.close()

    metadata = {}

    for line in lines:
        info = line.split(':')
        if len(info) == 2:
            metadata[sanitize(info[0])] = sanitize(info[1])

    return metadata
