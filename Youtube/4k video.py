from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex
import time
from bs4 import BeautifulSoup
import urllib.request

chrome = webdriver.ChromeOptions()


                   # put playlist address below and remove given address



link = 'https://www.youtube.com/watch?v=ChOhcHD8fBA'
#chrome.add_argument('--incognito')
browser = webdriver.Chrome(executable_path='chromedriver',chrome_options=chrome)
browser.get('http://youtubemultidownloader.com/index.html')
element = WebDriverWait(browser,50).until(lambda browser: browser.find_element_by_id('txtLink'))
time.sleep(3)
be = browser.find_element_by_id('txtLink')
be.send_keys(link)
element = WebDriverWait(browser,50).until(lambda browser: browser.find_element_by_xpath("//a[@class='btn btn-default']"))
data = browser.find_elements_by_partial_link_text('4K')
data[1].click()
element = WebDriverWait(browser,50).until(ex.visibility_of_element_located((By.XPATH,'//*[@id="Convert"]/div[2]/div[3]/a/button')))
button = browser.find_element_by_xpath("//a[@rel='noreferrer']")
print("Downloading Start ......")
browser.get(button.get_attribute('href'))
time.sleep(20)









