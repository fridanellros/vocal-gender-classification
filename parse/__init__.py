def paths(folder, sample):
    return( folder / sample / "wav", folder / sample / "etc" / "README")

def parse_readme(path) -> dict:

    r = open(path, "r")
    lines = r.readlines()
    r.close()

    metadata = {}

    for line in lines:
        info = line.split(':')
        if len(info) == 2:
            metadata[info[0].strip(' \n')] = info[1].strip(' \n')

    return metadata
