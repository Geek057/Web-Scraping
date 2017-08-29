import os
from ftplib import  FTP
ftp = FTP('www.domainname.com')
ftp.login('username','password')
ftp.cwd('/public_html')
data = []
ftp.dir(data.append)
[(str(i).split()[-1]) for i in data]
lis = []
for i in data:
    lis.extend([(str(i).split()[-1]) for i in data])


def getfile():
        for name in lis[3:]:
            ftp.retrbinary('RETR '+name,open(name,'wb').write,1024)
        ftp.quit()


getfile()
