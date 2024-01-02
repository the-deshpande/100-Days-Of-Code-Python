from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

env = dotenv_values()


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(webdriver.ChromeOptions().add_experimental_option('detach', True))

    def login(self):
        self.driver.get(url='https://www.instagram.com')

        sleep(2)
        self.driver.find_element(By.NAME, value='username').send_keys(env['EMAIL'])
        self.driver.find_element(By.NAME, value='password').send_keys(env['PASSWORD'], Keys.ENTER)

        sleep(5)

    def follow(self):
        self.driver.get(f'https://www.instagram.com/{env['ACCOUNT']}/followers')

        sleep(10)

        buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in buttons[:10]:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Unfollow')]").click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.follow()

