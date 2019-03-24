def paths(folder, sample):
    return( folder / sample / "wav", folder / sample / "etc" / "README")

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
