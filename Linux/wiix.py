import wiix_lib
import os
from wiix_lib import WiiX_CD, WiiX_Program

def nothing():
    print("\n\n")

WiiX_Program.SystemCommand("clear")
nothing()
print("WiiX 1.0 by Holia\n----------------------\n")

projectname = input("Enter a project name to create a HBC App : ")

WiiX_Program.CreateProjectFolder(projectname)

projectdir = "./Projects/" + projectname + "/"

with WiiX_CD(projectdir):
    path = os.path.abspath(os.getcwd())
    nothing()
    print("Current dir :\n")
    print(projectdir)
    nothing()
    dolfile = input("Link of boot.dol file (complete path) : ")
    WiiX_Program.SystemCommand("cp " + dolfile + " " + path)
    nothing()
    print("BOOT.DOL Path :\n")
    print(path + "/" + "boot.dol")
    nothing()
    iconfile = input("Link of icon.png file (complete path) : ")
    WiiX_Program.SystemCommand("cp " + iconfile + " " + path)
    print("ICON.PNG Path :\n")
    print(path + "/" + "icon.png")
    nothing()

    #namehbc = input("Name of your homebrew : ")
    #authbc = input("Your Author Name : ")
    #ver = input("Version of your homebrew : ")
    #date = "20210427150308" # Date can be modified if you want
    #desc = input("Description of your homebrew : ")

    
    #WiiX_Program.SystemCommand('echo <?xml version="1.0" encoding="UTF-8" standalone="yes"> > meta.xml')
    #WiiX_Program.SystemCommand('echo <app version="1"> >> meta.xml')
    #WiiX_Program.SystemCommand('echo      <name>' + namehbc +'</name> >> meta.xml') 
    #WiiX_Program.SystemCommand('echo      <version>' + ver + '</version> >> meta.xml')
    #WiiX_Program.SystemCommand('echo      <release_date>' + date + '</release_date> >> meta.xml')
    #WiiX_Program.SystemCommand('echo      <coder>' + authbc + '</coder> >> meta.xml')
    #WiiX_Program.SystemCommand('echo      <short_description>' + desc + '</short_description> >> meta.xml')
    #WiiX_Program.SystemCommand('echo      <long_description>' + namehbc + ' by ' + authbc + ' >> meta.xml')
    #WiiX_Program.SystemCommand('echo </long_description> >> meta.xml')
    #WiiX_Program.SystemCommand('echo <ahb_access/> >> meta.xml')
    #WiiX_Program.SystemCommand('echo </app> >> meta.xml') 

    #nothing()
    #print("Success ! Now zip the folder : " + projectdir + " and go to SDCARD:/apps/ and unzip !\nThanks to using WiiX")

    WiiX_Program.SystemCommand("cp ../../LinuxFiles/meta.sh " + path)
    WiiX_Program.ExecuteShell("meta.sh")

    print("Success ! Now zip the folder : " + projectdir + " and go to SDCARD:/apps/ and unzip !\nThanks to using WiiX")