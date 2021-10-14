'''

The main shell interpreter

'''


import os
import kernel.libc as libc

# process string
def process(stri: str):
    keys = stri.split(" ")
    if keys[0] == "cd":
        os.chdir(keys[1])
    if keys[0] == "mount":
        if len(keys) <= 2:
            print("usage: mount <disk> <dest> <options>")
            print('''
the MOUNT utility is a builtin system utility written in Python.
It's a direct call to the `mount` syscall on unix.

This command isn't supported on Windows, but instead of error-ing, it'll just not do anything. Sorry!
            ''')
        else:
            libc.mount(keys[1], keys[2], keys[3], keys[4] if len(keys) > 3 else "")