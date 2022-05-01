from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By
import pyautogui

twitterAccountsToSubscribe = ['danyliuk111110','danyliuk111111','danyliuk111112',
                              'danyliuk111113','danyliuk111114','danyliuk111115','danyliuk111116','danyliuk111117',
                              'danyliuk111118','danyliuk111119','danyliuk1111110','danyliuk1111112',
                              'danyliuk1111113','danyliuk1111114','danyliuk1111115','danyliuk1111116','danyliuk1111117']


logins = []
passwords = []
emails = []

with open('twitterAccounts2.txt','r') as accounts:
    for line in accounts:
        credential = line.split(':')
        logins.append(credential[0])
        passwords.append(credential[1])
        emails.append(credential[2])
        print(credential)

for i in range(3,13):
    service = Service("chromedriver.exe")
    service.start()
    option = webdriver.ChromeOptions()
    driver = webdriver.Remote(service.service_url, options=option)
    driver.get('https://twitter.com/i/flow/login')
    time.sleep(10)
    loginInput = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input').send_keys(logins[i])
    time.sleep(5)
    nextButton = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div').click()
    time.sleep(5)
    passwordInput = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(passwords[i])
    time.sleep(5)
    nextButton2 = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
    time.sleep(5)
    try:
        emailInput = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(emails[i])
        time.sleep(5)
        nextButton3 = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
    except:
        pass
    time.sleep(5)
    try:
        rightEmail = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div').click()
    except:
        pass

    for k in twitterAccountsToSubscribe:
        driver.get(f'https://twitter.com/{k}')
        time.sleep(random.random()+3)
        try:
            followChanel = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div').click()
        except:
            pass
        time.sleep(random.random() + 3)
    time.sleep(5)
    driver.quit()