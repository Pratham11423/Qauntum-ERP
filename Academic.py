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

# click on Academic
driver.find_element(By.XPATH,'//*[@id="body"]/form/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/img').click()
time.sleep(8)

# click on time table
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[1]/a').click()
time.sleep(8)

# click on assignment
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[2]/a').click()
time.sleep(8)

# click on syllabus
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[3]/a').click()
time.sleep(8)

# click on sem.-registration
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[5]/a').click()
time.sleep(8)
# click on ok
driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/button').click()
time.sleep(4)

# click on document apply
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[6]/a').click()
time.sleep(8)

# click on Achievement
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[7]/a').click()
time.sleep(8)

# click on apply for GP Marks
driver.find_element(By.XPATH,'//*[@id="sidebar-nav"]/ul/li[8]/a').click()
time.sleep(8)

# click on Home
driver.find_element(By.XPATH,'//*[@id="lnkReturn"]/img').click()
time.sleep(8)
