from sys import exit
from time import sleep
from os import getenv, system
from shutil import rmtree
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import load
from winreg import HKEY_CURRENT_USER, OpenKeyEx, QueryValueEx

repo = "lolmanurfunny/Roblox-Launcher-minus-the-app"

try:
    version = load(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag"))["clientVersionUpload"]
except:
    try:
        version = str(urlopen("http://setup.roblox.com/version.txt").read()).split("'")[1]
    except:
        key = OpenKeyEx(HKEY_CURRENT_USER, r"Software\ROBLOX Corporation\Environments\roblox-player\Versions")
        version = QueryValueEx(key, "version0")[0]

print("Client version hash: "+version)
filepath = getenv("LOCALAPPDATA")+"\\Roblox\\Versions\\"

def littleTimmyPrevention():
    input("Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\nDon't open a new issue regarding this if you installed Roblox to a non-User directory!")

debug = False
if exists(filepath) and not debug:
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=version
    if exists(filepath):
        print("Found \""+version+"\" folder!")
    else:
        print("[Error]: Unable to locate latest roblox client!")
        littleTimmyPrevention()
        exit(1)
else:
    print("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    littleTimmyPrevention()
    exit(1)

places = filepath+"\\ExtraContent\places"
UniversalApp = filepath+"\\ExtraContent\\LuaPackages\\UniversalApp"

ouch = filepath+"\\content\\sounds\\ouch.ogg"

if exists(places) and not debug:
    rmtree(places)
if exists(UniversalApp) and not debug:
    rmtree(UniversalApp)

oof = input("Would you like to return the oof sound back? [Y/N] ")

if oof.lower().strip() == "y":
    print("Installing oof sound...")
    urlretrieve("https://github.com/"+repo+"/raw/main/Audio/ouch.ogg",ouch)
    print("Successfully installed oof sound.")
elif oof.lower().strip() == "n":
    print("Skipping...")
else:
    print("You wrote neither \"Y\" nor \"N\". Skipping...")

print("This window will close in 3 seconds...")

for _ in range(3,0,-1):
    system("title "+"Closing in "+_.__str__())
    print(".", end="")
    sleep(1)
exit(0)
