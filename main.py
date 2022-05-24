from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import os
from selenium.webdriver.chrome.options import Options

mailService = 'https://generator.email/'
mainLink = 'https://rfer.al/RozTT_eoYzjBF'


with open('names.txt') as f:
    lines = f.read().split()

num = 0
num1 = 0
count = 1

while count<=50:

    try:
        link = 'chromedriver.exe'
        options = Options()
        options.add_extension('extension.crx')

        driver = webdriver.Chrome(link, chrome_options=options)

        driver.get("chrome-extension://oofgbpoabipfcfjapgnbbjjaenockbdp/popup.html")
        while(len(driver.window_handles) == 1):
            continue
        driver.switch_to_window(driver.window_handles[0])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="language-mode"]/div/div/div[2]/ul/li[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="codeBox1"]').send_keys('BZ4CQIHLUU')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="0in"]/a').click()
        time.sleep(2)

        fName = random.choice(lines)
        lines.remove(fName)


        lName = random.choice(lines)
        lines.remove(lName)

        Name = fName + ' ' + lName

        #dom = '@googleappsmail.com'
        dom = random.choice(['@robonx.com', '@robomedtech.com', '@googleappsmail.com', '@codespeech.com', '@gmailup.com', '@letsgotech.org'])

        email = fName + lName + dom
        p = fName + lName

        driver.get(mainLink)

        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(p)
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(fName)
        driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(lName)
        #time.sleep(1)
        driver.find_element_by_xpath('//*[@id="registration-form"]/button').click()


        time.sleep(4)

        driver.get(mailService + email)
        driver.find_element_by_link_text('Verify Email').click()

        time.sleep(6)

        driver.quit()
        num +=1

        print(count)

    except Exception:
        print(Exception)
        num1+=1
    finally:
        count+=1
        continue

print("Success = ", num)
print("Failed = ", num1)