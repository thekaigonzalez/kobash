import os
import sys
import pathlib

class EcoSystem:
    # name=The name of your ecosystem.
    # ps1= the prompt. Like the unix PS1 variable.
    def __init__(self, name, ps1) -> None:
        self.name = name
        self.prompt = ps1
    def Initialize(self):
        self.Init()
'''
myeco = EcoSystem("pygo", "-# ")

def MyEvent():
    print("hello, ecosystem!")

# Bind "Init" to my custom event.
myeco.Init = MyEvent

'''

def load():
    if pathlib.Path("handler.py").exists():
        import handler
        if (handler.startup) != None:
            handler.startup()
