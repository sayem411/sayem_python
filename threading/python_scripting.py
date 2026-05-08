#current working directory
import os

def current_directory():
    cwd=os.getcwd()
    print(cwd)

def file_path(filename):
    path=os.path.abspath((filename))
    print(path)

current_directory()
filename="sample.txt"
file_path(filename)

#time module
import time
epc=time.time()
print(epc)
localtime=time.localtime(epc)
print(localtime)
print(localtime.tm_year)
print(time.ctime(epc))

#mail transfer protocol









