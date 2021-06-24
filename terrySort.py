# Imports
from os import listdir
from os.path import isfile, join, isdir
import os.path
from tkinter import *
from PIL import ImageTk, Image
import os
from PIL import Image
from natsort import natsorted

# A function that returns an array of all the files in the specified folder
def fileArrayBuilder(folderPath):
    myFiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
    myFiles = natsorted(myFiles)
    print(myFiles)
    return myFiles

# A function that moves the specified file into the specified folder
def moveFile(fileName, folderName):
    dirName = "E:/.Trash-1000/files/Visuals/Pictures/"
    print("Moving " + dirName + fileName + " to " + dirName + folderName + "/" + fileName)
    os.rename(dirName + fileName, dirName + folderName + fileName)

# A function that gets the specified folder path and calls other functions
def startFunc():
    # Get folder path
    # Get file array
    # Get folder array
    # Call windowLooper with file and folder arrays
    # specifiedDir = input("Enter full path with drive letter of the folder you want to sort: ")
    specifiedDir = "E:/.Trash-1000/files/Visuals/Pictures"
    files = fileArrayBuilder(specifiedDir)
    fileLooper(files)
    
def fileLooper(files):
    for i in files:
        specifiedDir = "E:/.Trash-1000/files/Visuals/Pictures/"
        print(i)
        #im = Image.open(specifiedDir + i)
        #im.show()
        fol = input("Specify folder: ")
        moveFile(i, fol)

# Start the script
startFunc()