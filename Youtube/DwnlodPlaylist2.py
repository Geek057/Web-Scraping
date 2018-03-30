from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
import urllib.request

chrome = webdriver.ChromeOptions()


                   # put playlist address below and remove given address


link = 'https://www.youtube.com/playlist?list=PLZvdFvKxLm4aJAvv9TLGajO20ARHaVwfX'
chrome.add_argument('--incognito')
browser = webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome)
browser.get('http://youtubemultidownloader.com/playlist.html')
element = WebDriverWait(browser, 60).until(lambda browser: browser.find_element_by_id('txtPlaylist'))
time.sleep(5)
be = browser.find_element_by_id('txtPlaylist')
be.send_keys(link)
print('collecting all video........ ')
print('if your internet speed is slow then increase below sleep time ')
time.sleep(25)
data = browser.find_elements_by_link_text('MP4 720P')
for link in data:
    print('Downloading Video ........')
    browser.get(link.get_attribute('href'))
    time.sleep(10)
    print('Successfully Downloaded ......')



