import pathlib

def exists(path):
    if pathlib.Path(path).exists():
        return True
    else:
        return False

def isdir(path):
    return True if pathlib.Path(path).is_dir() else False