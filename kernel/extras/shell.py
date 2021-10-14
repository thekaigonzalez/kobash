# the shell executor for Kobash.

import kernel.http as http
import kernel.extras.shellinterpret as interp
import kernel.filesystem as kfs
import kernel.security.mask as mask
import os
import kernel.reader as kreader
import kernel.extras.toolkit as tk

def tmain():
    while (True):
        try:
            line = kreader.read(mask.pure_user() + "@" + os.getcwd() + "$ ")
            interp.process(line)
        except KeyboardInterrupt:
            print("logout")
            quit(1)