import os
import kernel.http
import argparse
import kernel.argparse as argparser
import zipfile



# Modified version of zip.py in KTerminal.
def Main(argv):
    if len(argv) < 1:
        print("zip: option required\nzip: usage: zip [-h] [FILE ...]")
        return 2
    if (argv[0] == "-h"):
        print("zip: usage: zip [-h] [FILE ...]")
    else:
        if len(argv) <= 1:
            print("zip: missing argument\nzip: usage: zip [-h] [FILE ...]")
            return 1; # kobash has return handlers. pretty sick!
        if len(argv) == 2:
            fn = zipfile.ZipFile(argv[0], 'w')
            fn.write(argv[1])
            fn.close()
            return 0; # kobash has return handlers. pretty sick!
        
    
    return 0