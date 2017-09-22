#! /usr/bin/python3

import imaplib
import email
import time
import getpass
import subprocess
import sys
readmail = imaplib.IMAP4_SSL('imap.gmail.com',993)
error = 0
readmail.login('username@gmail.com', 'password')

def check_email():
    try:
        readmail.select('INBOX')
        type, data = readmail.search(None, '(UNSEEN)')
        strn = data[0].decode('utf-8')
        email_id = strn.split()
        num = len(email_id)
        message = 'HI Your_name, '+'\n'+ 'You have '+str(num)+' unread email in mail box'
        subprocess.Popen(['notify-send', message])
    except Exception as f:
        print(f)


if __name__=='__main__':
    while(1):
      check_email()
      time.sleep(1800)






