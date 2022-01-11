from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
import os

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
driver.implicitly_wait(10)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"q")))

dog_Name = "한지민"   
# 강소라, 김태희, 김희선, 김혜수, 김희애, 손예진, 한가인, 송혜교, 한지민, 한효주 
os.makedirs("E:/Python Coding/selenium/연예인/여자 연예인/" + dog_Name)
# savePath = "E:/Python Coding/selenium/연예인/남자 연예인/"
savePath = "E:/Python Coding/selenium/연예인/여자 연예인/"

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(dog_Name + " 얼굴사진")
elem.send_keys(Keys.RETURN)

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == last_height:
        try:
            driver.find_element_by_css_selector("span.r0zKGf").click()
        except:
            try:
                driver.find_element_by_css_selector("input.mye4qd").click()
            except:
                break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1

for image in images:
    try:
        image.click()
        full_Name = str(dog_Name)+str(count) + ".jpg"
        # time.sleep(2)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_all_elements_located((By.ID, 'Sva75c')))
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute('src')
        urllib.request.urlretrieve(imgUrl, savePath + dog_Name + "/" + full_Name)
        count = count + 1
    except:
        pass

driver.close()