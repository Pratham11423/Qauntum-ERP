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

driver.find_element(By.XPATH,'//*[@id="UserName"]').send_keys("22****6")
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="Password"]').send_keys("******")
time.sleep(10)

# Login button
driver.find_element(By.XPATH,'//*[@id="login-box-inner"]/div[5]/div/button').click()
time.sleep(10)

# click on Dashboard
driver.find_element(By.XPATH,'//*[@id="lnkDashboard"]/img').click()
time.sleep(10)

# scroll
driver.execute_script("window.scrollTo(0,900 )")
driver.implicitly_wait(4)
time.sleep(4)

# click on sem attendence view
driver.find_element(By.XPATH,'//*[@id="btnYearSemWiseAttendance"]').click()
time.sleep(4)

driver.execute_script("window.scrollTo(900,1400 )")
driver.implicitly_wait(4)
time.sleep(4)

# today's attendence click view
driver.find_element(By.XPATH,'//*[@id="btnAttendanceToday"]').click()
time.sleep(6)

driver.execute_script("window.scrollTo(1400,1800 )")
driver.implicitly_wait(4)
time.sleep(4)

# click on month register dropdown
driver.find_element(By.XPATH,'//*[@id="ddlYear"]').click()
time.sleep(4)

# click on month
driver.find_element(By.XPATH,'//*[@id="ddlYear"]/option[4]').click()
time.sleep(4)

# click on view
driver.find_element(By.XPATH,'//*[@id="btnMonthRegister"]').click()
time.sleep(6)

