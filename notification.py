import random
from time import sleep
import subprocess

import os
os.chdir('/home/linux/Downloads')
fw = open('quotes.txt','r')
vocab = fw.read()
vocab = [str(lis).replace('\n','') for lis in vocab.split('|')]


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return



while(1):
    ind = random.randrange(0,len(vocab))
    sendmessage(vocab[ind])
    sleep(10)
