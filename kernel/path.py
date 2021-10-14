import pathlib

def exists(path):
    if pathlib.Path(path).exists():
        return True
    else:
        return False