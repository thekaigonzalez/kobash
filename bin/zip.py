import os
import kernel.http
import argparse
import kernel.argparse as argparser
import zipfile



# Modified version of zip.py in KTerminal.
def Main(argv):
    parser = argparser.ArgumentParser("zip")
    parser.add_argument("-O", "-output", default="a.zip")
    global arg
    arg = parser.parse_args(argv)
    
    """ ZIP FILE TEST """
    # fn = zipfile.ZipFile(arg.output, 'w')
    # fn.write("./usr/bin/cat.py")
    # fn.close()
    return 0