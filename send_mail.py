import smtplib
import email
from email.mime.text import MIMEText
from email.parser import Parser
from optparse import OptionParser
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.ehlo()
conn.login('username@gmail.com','password')


msg = MIMEMultipart()

with open('text.txt','r') as f:  # attach a text file 
    mass = MIMEText(f.read())
    f.close()
    msg.attach(mass)

with open('GOT.jpg','rb') as f:    #attach a image or audio file 
    img = MIMEImage(f.read())
    f.close()
    msg.attach(img)


msg['subject'] = 'Enter Subject' #enter subject
msg['from'] = 'FROM ' #Enter from email send 
msg['to'] = 'TO'  # To...


conn.sendmail('from','email id on which you want to send email',msg.as_string())
conn.quit()
