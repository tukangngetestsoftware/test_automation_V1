from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

#Alamat 1
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)
driver.find_element(By.ID, 'RESULT_FileUpload-10').send_keys("C:/Users/Adikrisna/Downloads/Visi dan Misi PTCS.jpg")

time.sleep(10)