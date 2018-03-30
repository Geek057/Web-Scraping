#! /usr/bin/python3

import time
import os
import urllib.request
import sys
import datetime
import requests
from tinytag import TinyTag
import re


os.chdir('/media/lnx/Hard Disk/Hollywood/')
lis = []
for path,name,file in os.walk(os.getcwd()):
    for link in file:
       if re.match('.+.mp4',link):
           try:
               os.chdir(path)
               lis = os.path.splitext(link)
               url = 'https://api.themoviedb.org/3/search/movie?query=' + lis[0] + '&api_key=4d3aa8d440b6b68022f2297fdd535e16'
               data = requests.get(url).json()
               for i in range(data['total_results']):
                   endlink = data['results'][i]['poster_path']
                   poster_link = 'http://image.tmdb.org/t/p/w780/' + endlink
                   print(str(lis[0]),"Poster Download Start....")
                   urllib.request.urlretrieve(poster_link, str(lis[0]) + '.jpg')
                   print("End...")
           except Exception as f:
               continue



       if re.search('.mkv',link):
           try:
               os.chdir(path)
               fis = os.path.splitext(link)
               url = 'https://api.themoviedb.org/3/search/movie?query=' + fis[0] + '&api_key=4d3aa8d440b6b68022f2297fdd535e16'
               data = requests.get(url).json()
               for i in range(data['total_results']):
                  endlink = data['results'][i]['poster_path']
                  poster_link = 'http://image.tmdb.org/t/p/w780/' + endlink
                  print(str(fis[0]), "Poster Download  Start...")
                  urllib.request.urlretrieve(poster_link, str(fis[0]) + '.jpg')
                  print('End...')

           except Exception as f:
               continue














