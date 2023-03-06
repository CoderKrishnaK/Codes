import os
from sys import *

def Directory_Watcher(Dir_Name):
    print("Inside Directory watcher Method")
    print("Name of Input Directory : ",Dir_Name)

    for foldername, subfolder, Filenames in os.walk(Dir_Name):
        print("Folder Name is : "+foldername)
        
        for subf in subfolder:
            print("Subfolder name of : "+foldername+" is "+subf)
        
        for fnames in Filenames:
            print("File inside folder "+foldername+" is "+fnames)
        
        print(" ")

def main():
    print("Directory Watcher Application")

    if(len(argv)!= 2):
        print("Insufficient Arguments")
        exit()

    if(argv[1] == "-h"):
        print("This Script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_Name Directory_Name")
        exit()

    Directory_Watcher(argv[1])   

if (__name__ == "__main__"):
    main()