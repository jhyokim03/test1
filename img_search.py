import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import urllib.request

search = input("이미지 검색 ====>")
f_Name = 'image'
number = 100
interval = 1

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt)

driver.get(f"https://www.google.com/search?q={search}&udm=2")
time.sleep(3)


firstImage = driver.find_element(By.CSS_SELECTOR, "h3.ob5Hkd > a")
firstImage.click()
time.sleep(3)

for i in range(number):
    try:
        time.sleep(interval)

        image = driver.find_element(By.CSS_SELECTOR,"#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.FyHeAf.iPVvYb" )
        imageSrc = image.get_attribute('src')

        if not os.path.exists('img'):
            os.makedirs('img')

        urllib.request.urlretrieve(imageSrc, f'img/{f_Name}_{i+1}.jpg')
    except:
        print(f'{i+1}번째 이미지 저장 오류 발생')
    else:
        print(f'{i+1}번째 이미지 저장 성공)')
    finally:
        nextButton = driver.find_element(By.CSS_SELECTOR, "#Sva75c > div.A8mJGd.NDuZHe > div.LrPjRb > div > div.BIB1wf.EIehLd.fHE6De.Emjfjd > c-wiz > div > div.XQEEtd.VTMWGb > div > div.HJRshd > button:nth-child(2) > div")
        nextButton.click()
driver.quit()

