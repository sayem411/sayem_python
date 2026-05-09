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

#------------------------------
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("Welcome to Python scripting")
        f.close()
dest="/Users/md.assayem/sayem_python/Problem-Solving/Problem-Solving/sayem_python/sample.txt"
createFile(dest)
print("File created")

#mail transfer protocol
import smtplib

smtobj = smtplib.SMTP('smtp.gmail.com',587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login('mdassayem0@gmail.com','rrcx geox kpqo iouh')
"""
App password
1. Google Account → Security
2. 2-Step Verification start
3. App Passwords → "Mail" select
Generate  → get 16-digit password 
 sitting this code-
"""
smtobj.sendmail("mdassayem0@gmail.com","253-35-349@diu.edu.bd",'Subject:SMTP check.\nNiloy dada ki obostha?')
smtobj.quit()




