import os
import kernel.filesystem as kfs
from kernel.current import WorkingDir
import kernel.path as kpath
import kernel.low as lowl

def pre_setup():
    Completed = True
    if not kpath.exists("etc"):
        Completed = False
        lowl.mkdir("etc");
    if not kpath.exists("bin"):
        Completed = False
        lowl.mkdir("bin")
    if os.getenv("KOBASH_HOME") is None:
        print("Setup: updating KOBASH_HOME environment...")
        os.environ["KOBASH_HOME"] = WorkingDir()
    if Completed:
        print("Setup: Clean!")
    else:
        print("Setup: Found corrupt directories. Fixed them.")
