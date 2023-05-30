from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="content"]/iframe'))
driver.find_element(By.ID, "datepicker").click()

#Cara 1
# driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[4]/a').click()
# driver.close()

#Cara 2
driver.find_element(By.ID, "datepicker").send_keys("01/04/2023")
time.sleep(4)
driver.close()