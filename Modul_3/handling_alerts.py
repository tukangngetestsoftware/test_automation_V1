from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

#Handling Alerts
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID, 'alertButton').click()
time.sleep(2)
driver.switch_to.alert.dismiss()