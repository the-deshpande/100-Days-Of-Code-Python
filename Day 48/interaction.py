from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_settings)
driver.get('https://secure-retreat-92358.herokuapp.com/')

time.sleep(1)
f_name = driver.find_element(By.NAME, value='fName')
f_name.send_keys('abc')

l_name = driver.find_element(By.NAME, value='lName')
l_name.send_keys('xyz')

email = driver.find_element(By.NAME, value='email')
email.send_keys('abc@xyz.com')

time.sleep(1)
signup = driver.find_element(By.CSS_SELECTOR, value='button')
signup.click()
