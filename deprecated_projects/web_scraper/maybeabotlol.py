import sys
print(sys.version)

site = input("Enter link (include http:// or https://): ")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PATH = "/Users/williserdman/Documents/python_playground/web_scraper/chromedriver" #change according to system as I didn't change my PATH variable

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
#chrome_options.add_argument("--incognito") #not sure what the point is #update: there's no point

driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

def connect_to_site(temp):
	try:
		source = driver.get(temp)

		main_input_box = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "content")))

		driver.implicitly_wait(5)
	except:
		print("connection failed or something on", site, "has changed")


connect_to_site(site)
main_input_box.clear()
main_input_box.send_keys("does this work lol")

driver.implicitly_wait(5)

driver.quit()


