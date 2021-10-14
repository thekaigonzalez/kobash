import os
import sys
import pathlib

def load():
    if pathlib.Path("handler.py").exists():
        import handler
        if (handler.startup) != None:
            handler.startup()