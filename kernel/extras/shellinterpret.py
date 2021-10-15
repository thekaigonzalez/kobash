'''

The main shell interpreter

'''


import os
import types
import kernel.python as mods
import importlib.util
import kernel.libc as libc
import kernel.processor as proc
import kernel.ecosystem as eco
import kernel.path as kp

# aliases change the command to the command it's binded to.
aliases = {

}

def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def loadPyFile(strPath, name):
    loader = importlib.machinery.SourceFileLoader(name, strPath)
    mod = types.ModuleType(loader.name)
    loader.exec_module(mod)
    return mod

# process string
def process(strit: str):
    for stri in strit.split(";"):
        keys = stri.split(" ")
        if keys[0] in aliases:
            
            keys[0] = aliases[keys[0]]
        if keys[0] == "cd":
            if (len(keys) < 2):
                print("cd: expected an argument")
            else:
                os.chdir(keys[1])
        elif keys[0] == "mount":
            if len(keys) <= 2:
                print("usage: mount <disk> <dest> <options>")
                print('''
    the MOUNT utility is a builtin system utility written in Python.
    It's a direct call to the `mount` syscall on unix.

    This command isn't supported on Windows, but instead of error-ing, it'll just not do anything. Sorry!
                ''')
        
            else:
                libc.mount(keys[1], keys[2], keys[3], keys[4] if len(keys) > 3 else "")
        elif keys[0] == "ls":
            try:
                if (len(keys) <= 1):
                    print(" ".join(os.listdir(".")))
                else:
                    print(" ".join(os.listdir(" ".join(keys[1:]))))
            except FileNotFoundError:
                print("ls: No such file or directory, '" + " ".join(keys[1:]) + "'")
        elif keys[0] == "alias":
            print("added " + keys[0] + " to aliases.")
            aliases[keys[1]] = "".join(keys[2:])
            print(aliases)
        elif keys[0] == "clear":
            if proc.is_windows:
                os.system("cls")
            else:
                os.system("clear")
        else:
            if (keys[0] != "./") or keys[0] != ".":
                if (kp.exists(keys[0])) and kp.isdir(keys[0]):
                    eco.load_module(keys[0], keys[1:])
                if (kp.exists("/usr/share/kobash/" + keys[0])) and kp.isdir("/usr/share/kobash/" + keys[0]):
                    eco.load_module("/usr/share/kobash/" + keys[0], keys[1:])
                if (kp.exists("bin/" + keys[0] + ".py")):
                    loadPyFile(os.getenv("KOBASH_HOME") + "/bin/" + keys[0] + ".py", os.getenv("KOBASH_HOME") + "/bin/" + keys[0] + ".py").Main(keys[1:])
                else:
                    if os.system(" ".join(keys)) != 0 and not is_tool(keys[0]):
                        print("kobash: there isn't an ecosystem, builtin, or any file with the name, '{}'".format(keys[0]))

