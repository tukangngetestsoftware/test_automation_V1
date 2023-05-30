from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://demoqa.com/select-menu")

#Old Style Selection
pilih = Select(driver.find_element(By.ID, "oldSelectMenu"))
pilih.select_by_visible_text("Yellow")

#Select one with typing
driver.find_element(By.ID, "selectOne").click()
pyautogui.typewrite("Prof.")
pyautogui.press("enter")