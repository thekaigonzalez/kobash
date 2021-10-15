import os
import sys
import pathlib
import requests

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

def load_handler_script():
    if pathlib.Path("handler.py").exists():
        import handler
        try:
            if (handler.startup) != None:
                handler.startup()
        except Exception:
            pass
