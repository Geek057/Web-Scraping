#! /usr/bin/python3

from ftplib import FTP
import os
f = FTP('www.domain.com')
f.login('username','password')
f.getwelcome()
f.cwd('/public_html')
data = []
f.dir(data.append)
filename = [str(i).split()[-1] for i in data]
#(filename)

def getfile(name):
    opn = open(name,'wb')
    f.retrbinary('RETR '+name,opn.write,1024)

def sendfile():
    name = input("ENTER FILE NAME: ")
    if os.path.isfile(name):
        f.storbinary('STOR '+name,open(name,'rb'))
    else:
        print("FIile not exits in current directory")

os.chdir('/home/linux/Downloads')
for i in filename:
    print(i)

print("Enter 1 for send file to server OR 2 to get file file from server")
val = int(input())
if val==1:
    sendfile()
elif val==2:
    num = int(input(("Enter file number ")))
    getfile(str(filename[num-1]))
else:
    print('Wrong command')





