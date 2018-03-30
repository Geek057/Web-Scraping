#! /usr/env/python3

import os
import socket
import requests
import re
from bs4 import BeautifulSoup


link = "https://www.w3schools.com/cssref/css_colors.asp"
data = requests.get(link)
data = BeautifulSoup(data.content,'html5lib')


lis = []
for tr in data.find_all('tr'):
    temp = []
    for tp in tr.find_all('a',{'target':"_blank"}):
        temp.append(tp.text)
    lis.append(temp)

print(lis)














