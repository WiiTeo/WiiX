import os
import time
import sys   

class WiiX_Program():
    def CreateProjectFolder(nameOfDir):
        directory = nameOfDir
        parent_dir = "./Projects/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    def SystemCommand(cmd):
        os.system(cmd)

    def ExecuteShell(shellprog):
        os.system("bash ./" + shellprog)


class WiiX_CD:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)