# Jai Shree Ram

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://qums.quantumuniversity.edu.in"
driver = webdriver.Chrome()
# driver = webdriver.Chrome('C:\BSPLAut\chromedriver.exe')
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(4)

driver.find_element(By.XPATH,'//*[@id="UserName"]').send_keys("22030016")
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="Password"]').send_keys("dhiman12345")
time.sleep(10)

# Login button
driver.find_element(By.XPATH,'//*[@id="login-box-inner"]/div[5]/div/button').click()
time.sleep(10)

