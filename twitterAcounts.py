from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By
import pyautogui

twitterAccountsToSubscribe = ['BinanceAcademy','coingecko','ZelenskyyUa',
                              'Ukraine','KyivIndependent','Podolyak_M','EuromaidanPress','olgatokariuk',
                              'mrsorokaa','NikaMelkozerova','ukraine_world','DmytroKuleba',
                              'MFA_Ukraine','UAWeapons','BorisJohnson','oleksiireznikov','lapatina_',
                              'HuobiGlobal','lesiavasylenko','GeneralStaffUA']


logins = []
passwords = []
emails = []
passwordsEmail = []

with open('accounts.txt','r') as accounts:
    for line in accounts:
        credential = line.split(':')
        logins.append(credential[0])
        passwords.append(credential[1])
        emails.append(credential[2])
        passwordsEmail.append(credential[3])
        print(credential)

for i in range(len(logins)):
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
    time.sleep(5)
    settingsButton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div').click()
    time.sleep(5)
    settingsPrivacyButton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[8]').click()
    time.sleep(5)
    profileProperty = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[2]/a/div').click()
    time.sleep(5)
    acceptPassword = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div/div[2]/div/input').send_keys(passwords[i])
    time.sleep(5)
    nextButton4 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div').click()
    time.sleep(5)
    try:
        username = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[1]/div').click()
        time.sleep(10)
        usernameInput = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[1]/label/div/div[2]/div/input')
        usernameInput.clear()
        usernameInput.send_keys(f'danyliuk11111{i+16}')
        time.sleep(5)
        nextButton5 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div/div').click()
        time.sleep(5)
    except:
        pass
    try:
        backButton1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[1]/div[2]/div[2]/div[1]/a/div/div/div').click()
        profileProperty = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[2]/a/div').click()
        time.sleep(5)
        acceptPassword = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div/div[2]/div/input').send_keys(passwords[i])
        time.sleep(5)
        nextButton4 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div').click()
        time.sleep(5)
    except:
        pass
    time.sleep(5)
    changeCountry = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[5]/div/div/div[1]').click()
    time.sleep(10)
    selectCountry = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[1]/select/option[225]')
    try:
        if selectCountry.text == 'Ukraine':
            selectCountry.click()
        else:
            selectCountry = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[1]/select/option[216]')
            selectCountry.click()
        time.sleep(5)
        confirmCountry = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div')
        confirmCountry.click()

    except:
        pass
    time.sleep(5)
    backButton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[1]/div/div/div/div/div[1]/div/div').click()
    time.sleep(5)
    changeGender = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[7]/div/div/div[1]').click()
    time.sleep(5)
    manGender = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[2]/div/div/label[2]/div/div[2]/input').click()
    time.sleep(5)
    acceptGender = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div').click()
    time.sleep(5)
    myProfile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
    time.sleep(5)
    editProfile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/a').click()
    time.sleep(5)
    try:
        changePhoto = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div').click()
        time.sleep(5)
        pyautogui.write(r'D:\pythonProjects\photo.jpg')  # path of File
        pyautogui.press('enter')
        time.sleep(5)
        confirmButton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div').click()
        time.sleep(5)
        nextButton6 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        time.sleep(5)
        skipBackground = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        time.sleep(5)
        skipBackground2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        time.sleep(5)
        seeprofile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div').click()
    except:
        pass
    time.sleep(5)
    try:
        myProfile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
        time.sleep(5)
        editProfile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/a').click()
        time.sleep(5)
    except:
        pass
    time.sleep(5)
    newName = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/label/div/div[2]/div/input')
    newName.clear()
    newName.send_keys('Mykhailo Danyliuk')
    editBirthday = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[7]/div[1]/div[3]/span').click()
    time.sleep(5)
    confirmBDedit = driver.find_element(By.XPATH,'//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]').click()
    time.sleep(5)
    try:
        deleteBD = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[7]/div[4]/div/div').click()
        time.sleep(5)
        confirmDeleting = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div').click()
    except:
        pass
    time.sleep(5)
    try:
        changePhoto = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div').click()
        time.sleep(5)
        pyautogui.write(r"D:\pythonProjects\photo.jpg") #path of File
        pyautogui.press('enter')
        time.sleep(5)
        confirmPhoto = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div')
        confirmPhoto.click()
        time.sleep(5)
    except:
        pass
    confirmEdition = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div')
    confirmEdition.click()
    time.sleep(5)


    # add followers
    time.sleep(5)
    try:
        driver.get(f'https://twitter.com/binance')
        time.sleep(5)
        subscribeBinance = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div').click()
        time.sleep(5)
        driver.get(f'https://twitter.com/ukraine')
        time.sleep(5)
        subscribeUkraine = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div').click()
    except:
        pass
    for k in twitterAccountsToSubscribe:
        driver.get(f'https://twitter.com/{k}')
        time.sleep(random.random()+3)
        try:
            followChanel = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/aside/div[2]/div[1]/div/div[2]/div/div[2]/div/div/span/span').click()
        except:
            pass
        time.sleep(random.random() + 3)
    time.sleep(5)

    with open('createdAccountsNum', 'a') as newUsers:
        newUsers.write('danyliuk11111' + str(int(i)+16) + ' ' + str(passwords[i]) + ' ' + str(emails[i]) + ' ' + str(passwordsEmail[i]))

    driver.quit()
