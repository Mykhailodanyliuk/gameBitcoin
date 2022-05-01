from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By

service = Service("chromedriver.exe")
service.start()
option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Remote(service.service_url, options=option)
driver.get('https://www.binance.com/en/activity/bitcoin-button-game')

time.sleep(10)

f = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div/div[4]/div[2]/div[1]/div[2]').text
print(f)

