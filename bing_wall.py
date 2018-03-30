#! /usr/bin/python3

import re
import os
import time
import json
import requests
import urllib.request

time.sleep(5)

URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

try:
    image_data = (requests.get(URL).json())
    image_url = 'http://www.bing.com' + image_data['images'][0]['url']
    # url for better quality image
    image_download_url = 'http://www.bing.com/hpwp/' + image_data['images'][0]['hsh']
    print(image_download_url)
    image_name = image_url[re.search("rb/", image_url).end():re.search('_EN', image_url).start()] + '.jpg'
    print(image_name)

    file_path = os.environ['HOME'] + '/Pictures/'+image_name
    if not os.path.exists(file_path):
        try:
            os.chdir(os.environ['HOME'] + '/Pictures/')

            # try downloading by first url(better quality)
            urllib.request.urlretrieve(image_download_url, image_name)
        except urllib.error.HTTPError:
            urllib.request.urlretrieve(image_url, filename=file_path)
        image_desc = image_data['images'][0]['copyright']
        print(image_desc)

        command = 'gsettings set org.gnome.desktop.background picture-uri file://' + file_path
        os.system(command)
        notify = 'notify-send -u critical "Wallpaper for the Day updated!" "' + image_desc + '"'
        os.system(notify)
    else:
        notify = 'notify-send -u critical "Bing Wallpaper" "Wallpaper for the day has been updated already!"'
        os.system(notify)

except:
    notify = 'notify-send -u critical "Bing Wallpaper" "Wallpaper can\'t be updated!"'
    os.system(notify)
