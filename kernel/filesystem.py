'''

The Filesystem.

Files will need to be created or removed, and this is a wrapper for that.

'''

import kernel.processor as processor

def kfile_new(fname, mode="w"):
    return open(fname, mode)
