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
"""
#mail transfer protocol
import smtplib

smtobj = smtplib.SMTP('smtp.gmail.com',587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login()
"""
#
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("Welcome to Python scripting")
        f.close()
dest="/Users/md.assayem/sayem_python/Problem-Solving/Problem-Solving/sayem_python/sample.txt"
createFile(dest)
print("File created")






