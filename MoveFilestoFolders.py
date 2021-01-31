from os import listdir
from os.path import isfile, join
import os
import shutil

# getFiles function will go through each files in the directory passed as arguement.
# Based the on the extension of the file, it will create the Directory and move the file into that directory.
# If directory is already created then it will directly copy the file into the exiting directory.

def getFiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        fileextension = i.split(".")[-1]
        if fileextension in i:
            if not os.path.exists(mypath+"\\"+fileextension.upper()):
                os.makedirs(mypath+"\\"+fileextension.upper())
                shutil.move(os.path.join(mypath, i), mypath + "\\"+fileextension.upper())
            else:
                shutil.move(os.path.join(mypath, i), mypath+"\\"+fileextension.upper())

path = "Put Path Here"
getFiles(path)