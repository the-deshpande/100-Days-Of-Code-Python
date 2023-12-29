from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

upcoming_events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery ul.menu li')

events = {}
for index, event in enumerate(upcoming_events):
    events[index] = {
        'time': event.find_element(By.CSS_SELECTOR, value='time').text,
        'name': event.find_element(By.CSS_SELECTOR, value='a').text,
    }

print(events)
driver.quit()
