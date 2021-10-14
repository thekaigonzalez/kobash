# mask User into randomized user until setup is completed.
# also generate a home directory.

import os
import sys
import getpass

# include kernel libraries

import kernel.filesystem as fs
import kernel.low as lowl
import kernel.plat as platform

def pure_user():
    return platform.origin_hostname()

def generate_home():
    lowl.mkdir("home/" + pure_user())
