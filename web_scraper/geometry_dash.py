
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "web_scraper/chromedriver"
SITE = "https://geometrydash.io"

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
source = driver.get(SITE)

app = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "game-play-area")))
time.sleep(10)
app.click()
time.sleep(10)
app.click()
