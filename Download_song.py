import requests
import os
import time
from bs4 import BeautifulSoup
import urllib.parse
print('Search your song:')
str = input()
str = '+'.join(str.split())
url = 'https://www.youtube.com/results?search_query='+str
data = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
data = BeautifulSoup(data.content,'lxml')
#data = data.prettify()
title = {}
for tit in data.find_all('a',{'class':'yt-uix-tile-link'}):
    title[tit.get_text()] = tit.get('href')

for i,k in enumerate(title.items()):
    print(i+1,k[0])

print('Song number to download: ')
num = int(input())
song_name = list(title.keys())[num-1]
download_link = list(title.values())[num-1]
print('Downloading...')
os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com' + download_link)





