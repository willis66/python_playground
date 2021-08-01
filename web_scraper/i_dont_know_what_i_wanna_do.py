
site = "https://google.com"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

source = driver.get(site)

main_input_box = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "q")))#by site

driver.implicitly_wait(5)

main_input_box.clear()
main_input_box.send_keys("does this work lol")

driver.implicitly_wait(5)

driver.quit()