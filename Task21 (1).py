#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)
time.sleep(4)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(4)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(4)
driver.find_element(By.ID, "login-button").click()

time.sleep(4)

#cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

time.sleep(4)
#menu button
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(4)

#logout
driver.find_element(By.ID,"logout_sidebar_link").click()

time.sleep(3)

driver.close()


# In[ ]:




