'''

The main shell interpreter

'''


import os

# process string
def process(stri: str):
    keys = stri.split(" ")
    if keys[0] == "cd":
        os.chdir(keys[1])
    