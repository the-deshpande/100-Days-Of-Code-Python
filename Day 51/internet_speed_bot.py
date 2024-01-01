from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import dotenv_values

env = dotenv_values()

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(webdriver.ChromeOptions().add_experimental_option('detach', True))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net')
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value='button#onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CSS_SELECTOR, value='span.start-text').click()
        sleep(60)
        self.down, self.up = [float(i.text) for i in self.driver.find_elements(By.CSS_SELECTOR,
                                                                               value='div.result-data span')[2:4]]

    def tweet_internet_speed(self):
        self.driver.get(url='https://twitter.com/login')
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, value='input').send_keys(env['TWITTER_EMAIL'], Keys.ENTER)
        sleep(5)
        location = ('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                    '3]/div/label/div/div[2]/div[1]/input')
        try:
            self.driver.find_element(By.XPATH, value=location).send_keys(env['TWITTER_PASSWORD'], Keys.ENTER)
        except NoSuchElementException:
            self.driver.find_element(By.CSS_SELECTOR, value='input').send_keys(env['USERNAME'], Keys.ENTER)
            sleep(5)
            self.driver.find_element(By.XPATH, value=location).send_keys(env['TWITTER_PASSWORD'], Keys.ENTER)

        message = (f"Hi everyone, this is a python bot\n"
                   f"My current internet speed is\n"
                   f"Download : {self.down}Mbps\n"
                   f"Upload : {self.up}Mbps")
        sleep(5)
        location = ('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                    '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div['
                    '1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.driver.find_element(By.XPATH, value=location).send_keys(message)
        location = ('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                    '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        self.driver.find_element(By.XPATH, value=location).click()

        sleep(5)
        print("The tweet is posted!")

