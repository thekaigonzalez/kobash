import os
import sys
import kernel.processor as pr

def tty():
    '''
    returns TTY name on Linux systems.
    If OS is not Linux, it will return "CMD".
    '''
    if not pr.is_windows:
        return os.ttyname(sys.stdout.fileno())
    else:
        return "CMD"