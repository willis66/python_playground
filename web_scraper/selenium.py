
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)

query = "hello world"
DRIVER.get("https://google.com")
print(DRIVER.title)

search = DRIVER.find_element_by_name('q')
search.send_keys("hello world")
search.send_keys(Keys.RETURN)

results = []

for i in range(10):
    results.append(DRIVER.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/a"))

print(results)

time.sleep(5)

#results = DRIVER.find_element_by_class_name("LC20lb DKV0Md")

time.sleep(2)

DRIVER.quit()
