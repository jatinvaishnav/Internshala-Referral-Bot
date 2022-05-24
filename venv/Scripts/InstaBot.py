from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import os
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

link = 'D:\\Softwares\\chromedriver.exe'

driver = webdriver.Chrome(link, options=options)

driver.get("https://www.instagram.com/")

time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("furqaanhashim@gmail.com")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("200900030901QWE!@#")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[4]/button').click()

count = 0
code = 99999999


while 1:
    try:
        codeT = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[1]/div/label/input')
        codeT.send_keys(code)
        print(code)

        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[2]/button').click()

        break

        code -= 1

    except Exception as e:
        print("EXCPPTION ", e)
        count += 1
        break