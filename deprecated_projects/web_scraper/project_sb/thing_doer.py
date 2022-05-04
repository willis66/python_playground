
#Mainly online, so asnyc is going to be really important
import asyncio

#Saving data
import pickle

#Using Selenium to operate the webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import time

#These are the sites that are going to be visited
SB_MAIN = "https://www.swagbucks.com"
SB_LOGIN = "https://www.swagbucks.com/p/login"
SB_WATCH = "https://www.swagbucks.com/watch"
TEMP_MAIL = "https://temp-mail.org/en"
PASSWORD = "Willisg612"

#Some ID's within the SB site
EMAIL_SIGNUP_ID = "sbxJxRegEmail"
PASS1_SIGNUP_ID = "sbxJxRegPswd"
PASS2_SIGNUP_ID = "sbxJxRegEmailConfirm"

PATH = "/Users/williserdman/Documents/python_playground/web_scraper/chromedriver"

#Doesn't send data to the website that we're visiting that it's a bot/automated software
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#chrome_options.add_argument("--incognito")

class Account():

	def __init__(self):
		self.email = None
		self.sc_num = None
		self.driver = uc.Chrome(executable_path=PATH, options=chrome_options)

	################ NEW TAB NOT WORKING #################
	def new_tab(self):
		#This will open a new tab
		#self.driver.execute_script('''window.open("", "_blank");''')
		#ActionChains(self.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
		#You can use (Keys.CONTROL + 't') on other OSs
		return


	def get_mail(self):
		#This establishes the website we're going to visit
		source = self.driver.get(TEMP_MAIL)
		EMAIL_ID = "//* [@id = 'mail']"

		#Making sure it's definitely loaded
		time.sleep(5)
		email_input_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, EMAIL_ID)))

		#Lastly getting the email as a string
		email_box = self.driver.find_element(By.XPATH, EMAIL_ID)
		self.email = email_box.get_attribute("value")

		print("email:", self.email)

	def create_sc_acc(self):
		#Going to the website
		source = self.driver.get(SB_MAIN)

		#Accesing the email address box
		email_input_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, EMAIL_SIGNUP_ID)))
		email_input_box.clear()
		email_input_box.send_keys(self.email)

		#Inputting password
		pass_initial = self.driver.find_element(By.ID, PASS1_SIGNUP_ID)
		pass_initial.clear()
		pass_initial.send_keys(PASSWORD)
		pass_confirm = self.driver.find_element(By.ID, PASS2_SIGNUP_ID)
		pass_confirm.clear()
		pass_confirm.send_keys(PASSWORD)

		#Hitting enter
		pass_confirm.send_keys(Keys.RETURN)

		time.sleep(5)

		#Going back to the homepage as it starts with "onboarding"
		temp = self.driver.get(SB_MAIN)

	def sign_into_acc(self):
		source = self.driver.get(SB_LOGIN)

		#Email
		email_input_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, EMAIL_SIGNUP_ID)))
		email_input_box.clear()
		email_input_box.send_keys("willis.erdman@gmail.com")

		#Password
		pass_initial = self.driver.find_element(By.ID, PASS1_SIGNUP_ID)
		pass_initial.clear()
		pass_initial.send_keys(PASSWORD)

		#Enter
		pass_initial.send_keys(Keys.RETURN)

		time.sleep(20)

	def watch_stuff(self):
		source = self.driver.get(SB_WATCH)

		time.sleep(15)
		#content2click = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "placementCard ng-scope")))
		#content2click = self.driver.find_element(By.CLASS_NAME, "placementCard ng-scope")
		content2click = self.driver.find_elements_by_class_name("placementCard ng-scope")
		content2click[0].click()

		while True:
			more_redirects = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "startEarning")))
			time.sleep(45)
			self.driver.close()




accounts = []
accounts.append(Account())
#accounts[0].get_mail()
#accounts[0].new_tab()
#accounts[0].create_sc_acc()
accounts[0].sign_into_acc()
time.sleep(20)
accounts[0].watch_stuff()

#Need to create a dictionary for all things that can link the account and the number of SB's

#ac1.driver.quit()
#c2.driver.quit()

