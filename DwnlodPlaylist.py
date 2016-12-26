from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
import time

print('If subtitle Present in any video then video not to be download ')
chrome = webdriver.ChromeOptions()

           # put playlist address below and remove given address


link = 'https://www.youtube.com/playlist?list=PLZvdFvKxLm4YCdyswFi-LNuKiEzVByVJ5'
href = []
chrome.add_argument('--incognito')
browser = webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome)
browser.get("http://9xbuddy.com/save?url="+str(link))
element = WebDriverWait(browser,20).until(lambda browser: browser.find_elements_by_xpath("//div[@class='playlist-title']"))
data = browser.find_elements_by_xpath("//div[@class='playlist-title']")
for i in data:
    xml = browser.find_element_by_link_text(str(i.text))
    href.append(xml.get_attribute('href'))
print('Download all video in 720 : Press "1",  Else Press "2"')
number = int(input())
if number==1:
    for p in href:
        browser.get(str(p))
        element = WebDriverWait(browser,60).until(lambda browser: browser.find_elements_by_link_text('Download Now'))
        download = browser.find_elements_by_link_text('Download Now')
        print('DOWNLOADING START ........')
        browser.get(download[0].get_attribute('href'))
        time.sleep(7)
        print('SUCCESSFULLY DOWNLOADED ..')

else:
    for p in href:
      browser.get(str(p))
      element = WebDriverWait(browser,60).until(ex.visibility_of_element_located((By.XPATH,"//li[@class='link-quality']")))
      quality  = browser.find_elements_by_class_name('link-quality')
      for qua in quality:
        print(qua.text)
      print('1 For 720p, 2 for 360p....')
      no = int(input())
      if no==1:
        download = browser.find_elements_by_link_text('Download Now')
        print('DOWNLOADING START ........')
        browser.get(download[0].get_attribute('href'))
        time.sleep(7)
        print('SUCCESSFULLY DOWNLOADED ..')
      elif no==2:
        download = browser.find_elements_by_link_text('Download Now')
        print('DOWNLOADING START ........')
        browser.get(download[1].get_attribute('href'))
        time.sleep(7)
        print('SUCCESSFULLY DOWNLOADED ..')
