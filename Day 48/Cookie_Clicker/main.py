from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_settings)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')
money = driver.find_element(By.ID, value='money')

start_time = time.time()
end_time = start_time + 60*5
interval = 7.5
last_interval = start_time

shops = [shop.get_attribute('id') for shop in driver.find_elements(By.CSS_SELECTOR, '#store div')[:-1]]

while True:
    cookie.click()

    if last_interval + interval < time.time():
        last_interval += interval

        cost = [int(price.text.split(" - ")[-1].replace(',', ''))
                for price in driver.find_elements(By.CSS_SELECTOR, '#store div b')[:-1]]
        prices = list(zip(shops, cost))
        prices.sort(key=lambda x: x[-1])

        wallet = int(money.text.replace(',', ''))

        if wallet >= prices[0][-1]:
            for index, price in enumerate(prices):
                if price[-1] > wallet:
                    print(wallet, prices[index-1])
                    driver.find_element(By.ID, value=prices[index-1][0]).click()
                    break

    if end_time < time.time():
        break

print(driver.find_element(By.ID, value='cps').text)
driver.quit()
