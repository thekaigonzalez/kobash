# wrapper around python.platform


import platform
import getpass

def origin_hostname():
    return getpass.getuser()

def origin_hardname():
    return platform.node()