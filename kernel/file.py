from io import TextIOWrapper
import os
import sys

def oneLine(file: TextIOWrapper):
    return file.readlines()[0]
