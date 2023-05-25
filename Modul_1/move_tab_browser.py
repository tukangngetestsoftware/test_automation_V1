from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.FirefoxOptions()
options.set_preference("devtools.console.stdout.content", True)

driver = webdriver.Firefox(options=options)

handles = driver.window_handles

# Pindah tab browser

driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT, 'Click Here').click()
time.sleep(3)
driver.switch_to.window(handles[0])

# Melanjutkan tindakan lainnya...

driver.quit()