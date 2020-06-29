import sys
import os

def listdir(folder_path):
    dirs = os.listdir(folder_path)
    for dir in dirs:
        print(dir)
        subpath = folder_path + "/" + dir
        if os.path.isdir(subpath):
            listdir(subpath)

try:
    dir = sys.argv[1]
    listdir(dir)
except:
    print("invalid directory")
