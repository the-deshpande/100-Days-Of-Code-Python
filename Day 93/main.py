from time import sleep
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import smtplib

env = dotenv_values()

URL = 'https://store.steampowered.com/'


class SteamGameData:
    def __init__(self):
        self.driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_experimental_option(
            'detach', True))
        self.game_data = {
            'summary': 'Generic Game',
            'price': '0',
            'details': ['TITLE: HELLO', 'Hello', 'Hi']
        }

    def get_game_data(self, game_name: str):
        self.driver.get(url=URL)
        sleep(2)

        search_bar = self.driver.find_element(By.CSS_SELECTOR, value='#store_nav_search_term')
        search_bar.click()

        search_bar.send_keys(game_name)
        sleep(1)
        search_bar.send_keys(Keys.DOWN)
        search_bar.send_keys(Keys.ENTER)

        sleep(1)
        try:
            self.game_data = {
                'summary': self.driver.find_element(By.CSS_SELECTOR, value='.game_description_snippet').text,
                'price': self.driver.find_element(By.CSS_SELECTOR, value='.game_purchase_price').text[2:],
                'details': self.driver.find_element(By.CSS_SELECTOR, value='.details_block').text.split('\n')
            }
        except Exception as e:
            print(e)

        self.driver.close()

    def mail_game_data(self):

        message = (f"Subject: Game Data \n\n"
                   f"Hi everyone, this is a python bot, providing game details from steam"
                   f"\n{self.game_data['details'][0]}"
                   f"\nPRICE: {self.game_data['price']}"
                   f"\nSUMMARY: {self.game_data['summary']}"
                   f"\n{'\n'.join(self.game_data['details'][1:])}")


        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=env['EMAIL'], password=env['PASSWORD'])
            connection.sendmail(from_addr=env['EMAIL'], to_addrs=env['RECEIVER'], msg=message)

        print('mail sent')


if __name__ == '__main__':
    bot = SteamGameData()
    bot.get_game_data('Palworld')
    bot.mail_game_data()
