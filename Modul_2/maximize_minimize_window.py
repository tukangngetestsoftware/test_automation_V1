from selenium import webdriver
import time

options = webdriver.FirefoxOptions()
options.set_preference("devtools.console.stdout.content", True)

driver = webdriver.Firefox(options=options)

handles = driver.window_handles

# Maximize Window
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

# Minimize Window
driver.get('https://www.google.com/')
driver.minimize_window()
time.sleep(3)
