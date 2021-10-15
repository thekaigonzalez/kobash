# PyGo is one of the main libraries that come with Kobash.
# no kernel APIs used due to portability.

import pygo.pygo_release as pygo

def Main(argv):
    looped = True
    # Main PyGo REPL
    print("PyGo utility")
    while looped:
        pygoterm = input("-# ")

        argv = pygoterm.split(" ")

        if (argv[0] == "pygo"):
            if (argv[1] == "-v"):
                print("PyGo version {}".format(pygo.VERSION_PYGO))