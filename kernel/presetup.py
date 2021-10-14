import kernel.filesystem as kfs
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
    if Completed:
        print("Setup: Clean!")
    else:
        print("Setup: Found corrupt directories. Fixed them.")
