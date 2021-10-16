#package handler


#(REPLACEMENT FOR SUDO. SUDO DOES NOT WORK AS WELL. AND IS ABANDONED AND DEPRECATED)
import curses
import importlib
import os

import time
import requests


def install(url):
    c = requests.Request("GET", url)
    return c.data


def Main(a):
    c = len(a)
    if c == 0:
        print("PKG for KTerminal.\nPorted By Kai D. Gonzalez to Kobash Python.\nUse pkg install to begin.")
    elif c >= 1:
        if a[0] == "install":

            link_base = "http://github.com/Kai-Builder/" + a[1]
            link_unixbinutils = "https://raw.githubusercontent.com/thekaigonzalez/unix-core/master/" + a[1] + ".py"
            link_base_rawcontentlink = "http://raw.githubusercontent.com/Kai-Builder/" + a[1]
            link_external = "http://github.com/" + a[1]
            link_external_rawcontentlink = "http://raw.githubusercontent.com/" + a[1] + ""
            request = requests.get(link_base)

            print("Looking for package {}...\n".format(a[1]))
            time.sleep(1)
            print("reading database for {}\n".format(a[1]))
            time.sleep(0.8)
            if requests.get(link_unixbinutils).status_code == 200:
                print("# installing module from unix-binutil\n")
                re = requests.request('GET', link_unixbinutils)
                u = open('usr/bin/' + link_unixbinutils[link_unixbinutils.rfind('/')+1:len(link_unixbinutils)], 'w')
                u.write(re.text)
                u.close()
            if request.status_code == 200:
                print("module found in verified area, checking for module's name ({}.py)\n ".format(a[1]))
                daak = requests.get(link_base_rawcontentlink + "/master/" + a[1] + ".py")
                if daak.status_code == 200:
                    print("Treating {} as an official module. downloading content. ..\n".format(a[1]))
                    time.sleep(2)
                    c = requests.request('GET', link_base_rawcontentlink + "/master/" + a[1] + ".py")
                    d = open("bin/" + a[1] + ".py", 'w')
                    d.write("#----------- BEGIN GENERATED LINE --------------#\nOFFICIAL=False\n#---------- END GENERATED LINE ----------#\n\n" + c.text)
                    d.close()
                    print("Success!\n")
                    time.sleep(1)
                    daak = requests.get(link_base_rawcontentlink + "/master/" + "deps.txt")
                    if daak.status_code == 200:
                        print("installing dependencies for " + a[1] + "\n")
                        time.sleep(0.5)
                        dep = open('cache-deps.txt', 'w')
                        dep.write(daak.text)
                        dep.close()
                        deps = open('cache-deps.txt', 'r')
                        ar = deps.readlines()
                        for i in ar:
                            os.system('pip3 install ' + i)
                        deps.close()
                        os.rmdir('cache-deps.txt')
                    else:
                        print(a[1] + " does not require any more dependencies. install success\n")

            else:
                print("Failed to find the module in verified space. checking for module as a github repository.\n")
                req = requests.get(link_external)
                if req.status_code == 200:
                    print("Module found as GitHub repository. Installing. . .\n")
                    time.sleep(2)
                    c = requests.request('GET', link_external_rawcontentlink + "/master/" + a[1] + ".py")
                    d = open("usr/bin/" + a[1] + ".py", 'w')
                    d.write(c.text)
                    d.close()
                    print("Success!\n")
                else:
                    print("module for {} not found.\n".format(a[1]))
        elif a[0] == "-u":
            try:
                if importlib.import_module("bin." + a[1]).OFFICIAL == True:
                    print("get-apt: cannot delete system module\n")
                else:
                    try:
                        print("deleting " + a[1] + "...\n")
                        os.remove("usr/bin/" + a[1] + ".py")
                    except Exception:
                        print("")
            except Exception:
                print("apt-get: cannot delete system module\n")