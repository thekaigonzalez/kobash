# version dependent on files.
# etc/release - release info
# etc/kernel - kernel info

import kernel.file as f
from pathlib import Path
release = ""
kernel_release = ""

def updateVersion():
    
    if (Path("etc/release").exists()):
        release = f.oneLine(open("etc/release"))

    if (Path("etc/kernel").exists()):
        kernel_release = f.oneLine(open("etc/kernel"))

