# the shell executor for Kobash.

import kernel.http as http
from colorama import Fore, Back, Style
import kernel.extras.shellinterpret as interp
import kernel.filesystem as kfs
import kernel.security.mask as mask
import kernel.current as cur
import os
import kernel.reader as kreader
import kernel.extras.toolkit as tk

def tmain():
    while (True):
        try:
            line = kreader.read(Style.BRIGHT + Fore.RED + mask.pure_user() + Style.RESET_ALL + "@" + Style.BRIGHT + Fore.GREEN + cur.WorkingDir() + "$ " + Style.RESET_ALL)
            interp.process(line)
        except KeyboardInterrupt:
            print("logout")
            quit(1)