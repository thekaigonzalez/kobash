# Ecosystems

'''

An "EcoSystem" is a part of a Kernel which is like a "mother ship" to all other subcommands.

Later on users will install other Ecosystems to gain access to other commands

This is an extension that comes with Kobash by default. It compliments the customizability features.

'''

import kernel.extras.toolkit as tk
import kernel.python as kpy

# Ecosystems are now officially a part of Kobash!

# You'll be using ecosystems a LOT, get familiar with them!

def load_module(strL: str, argvz):
    mod = kpy.kernelModule(strL)
    if (mod == None):
        return;
    else:
        mod.Main(argvz)