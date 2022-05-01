import datetime

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import requests
import time
import pygame
import random
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

twitterDict = {
                '8': {'login': 'danyliuk111117',
                     'password': 'lxuus6qycg',
                     'mail': 'cardenselene_1989+57@hotmail.com'},
                '9': {'login': 'danyliuk111118',
                     'password': '0mfofotder',
                     'mail': 'slatondorie1997+51@hotmail.com'},
                '10': {'login': 'danyliuk111119',
                     'password': 'hslhcs0tap',
                     'mail': 'mossmadonna_1990+69@hotmail.com:v8t6hOy5q'},
                '11': {'login': 'danyliuk1111110',
                     'password': 'gy8q2vbju6',
                     'mail': 'saucedokarri_1997+83@hotmail.com'},
                '12': {'login': 'danyliuk1111112',
                     'password': 'xr890s5sbm',
                     'mail': 'lytleguy_1989+70@hotmail.com'},
                '13': {'login': 'danyliuk1111113',
                     'password': 'pfr8smot2b',
                     'mail': 'pulleybranda2001+79@hotmail.com'},
                '14': {'login': 'danyliuk1111114',
                     'password': 'iivft25d0z',
                     'mail': 'cranfordeddie_2002+17@hotmail.com'},
                '15': {'login': 'danyliuk1111115',
                     'password': 'gjbc2hnjnf',
                     'mail': 'rosewillene_1995+69@hotmail.com'},
                '16': {'login': 'danyliuk1111116',
                     'password': 'zu8qvz8bpp',
                     'mail': 'raglandmaxwell1999+33@hotmail.com'},
                '17': {'login': 'danyliuk111117',
                     'password': 'i3n2vcn512',
                     'mail': 'camaraethyl2000+27@hotmail.com'},

               }



for i in twitterDict:
    print(twitterDict[f'{i}']['password'])

    isFinish = True
    while isFinish:
        ua = UserAgent()
        userAgent = ua.random

        try :
            service = Service("chromedriver.exe")
            service.start()
            option = webdriver.ChromeOptions()
            option.add_argument(f'user-agent={userAgent}')
            # option.add_argument('headless')
            driver = webdriver.Remote(service.service_url, options=option)
            driver.get('https://www.binance.com/en/activity/bitcoin-button-game')
        except:
            # pygame.mixer.init()
            # pygame.mixer.music.load('soda.mp3')
            # pygame.mixer.music.play(0)
            time.sleep(20)
            # pygame.mixer.music.stop()
            continue
        time.sleep(2)
        try:
            acceptCookies = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
            acceptCookies.click()
        except:
            pass
        signIn = driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[2]/div/div[1]/div[2]')
        signIn.click()
        time.sleep(5)
        termAndConditions = driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[3]/div/div[4]/label/div[1]')
        termAndConditions.click()
        time.sleep(0.5+random.random())
        twitterButton = driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[3]/div/div[3]/div[1]/div[4]/div/div/button/div[4]')
        twitterButton.click()
        time.sleep(2)
        login = driver.find_element(By.XPATH,'//*[@id="username_or_email"]')
        login.send_keys(twitterDict[f'{i}']['login'])
        time.sleep(0.5+random.random())
        password = driver.find_element(By.XPATH,'//*[@id="password"]')
        password.send_keys(twitterDict[f'{i}']['password'])
        time.sleep(0.5+random.random())
        loginButtonTwitter = driver.find_element(By.XPATH,'//*[@id="allow"]')
        loginButtonTwitter.click()
        try :
            mailInput = driver.find_element(By.XPATH,'//*[@id="challenge_response"]')
            mailInput.send_keys(twitterDict[f'{i}']['mail'])
            twitterMailButton = driver.find_element(By.XPATH,'//*[@id="email_challenge_submit"]')
            twitterMailButton.click()
        except:
            time.sleep(5)

        try :
            authorizeButton = driver.find_element(By.XPATH,'//*[@id="allow"]')
            time.sleep(0.5+random.random())
            authorizeButton.click()
        except :
            time.sleep(5)
        print('Logged')
        time.sleep(5)





        try:
            while True:
                k = datetime.datetime.now()
                if k.strftime("%M%S") == '0000' or k.strftime("%M%S") == '0001':
                    f = open('timeBitcoin.txt', 'a')
                    totalPeople = driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[3]/div[4]/div/div[4]/div[2]/div[2]/div[2]').text
                    f.write(k.strftime("%m/%d %%H:%M") + ' ' + totalPeople + '\n')

                c1 = BeautifulSoup(driver.page_source, "lxml")
                # driver.quit()
                c2 = c1.find('div', id='__APP')
                c3 = c2.find('div', class_='css-1lb294d')
                c4 = c3.find('div', class_='css-yi50lq')
                c5 = c4.find('div', class_='css-1xr3i7a')
                c6 = c5.find_all('div', class_='css-1ovrcs2')
                time12 = []
                for n in c6:
                    c71 = n.find_all('div', class_='css-1a1tjqj')
                    for m in c71:
                        c81 = m.find('div', class_='css-h5twer')
                        time12.append(c81.find('div', class_='css-w39bvu').text)

                print(time12[0]+time12[1]+time12[3])
                bitcoinButton = loginButtonTwitter = driver.find_element(By.XPATH,'//*[@id="__APP"]/div[2]/div[3]/div[5]/div/div[1]')
                print(float(time12[0])*10+float(time12[1])+float(time12[3])/10)
                if int(time12[0])*10+int(time12[1]) < 12 and  int(time12[0])*10+int(time12[1]) >= 10:
                    driver.refresh()
                    continue

                elif float(time12[0])*10+float(time12[1])+float(time12[3])/10 <= 1.5:
                    bitcoinButton.click()
                    time.sleep(3)
                    f = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div/div[4]/div[2]/div[1]/div[2]').text
                    # pygame.mixer.init()
                    # pygame.mixer.music.load('50.mp3')
                    # pygame.mixer.music.play(0)
                    # pygame.mixer.music.stop()
                    if f != '--':
                        with open('deletedAccounts', 'a') as file:
                            file.write(twitterDict[f'{i}']['login'])
                        time.sleep(50)
                        break

                else:
                    time.sleep(0.3)


        except:
            # pygame.mixer.init()
            # pygame.mixer.music.load('soda.mp3')
            # pygame.mixer.music.play(0)
            time.sleep(10)
            # pygame.mixer.music.stop()

        isFinish = False







