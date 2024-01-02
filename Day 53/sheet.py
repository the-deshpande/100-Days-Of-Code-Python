from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Sheet:
    def __init__(self):
        self.driver = webdriver.Chrome(webdriver.ChromeOptions().add_experimental_option('detach', True))

    def fill_the_form(self, url: str, details: dict):
        self.driver.get(url)
        sleep(1)

        location = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.driver.find_element(By.XPATH, location).send_keys(details['address'])

        location = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.driver.find_element(By.XPATH, location).send_keys(details['price'])

        location = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.driver.find_element(By.XPATH, location).send_keys(details['link'])

        sleep(1)
        self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

