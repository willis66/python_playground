
from bs4 import BeautifulSoup as bs
import requests
import re

PARSER = 'html.parser'

source = requests.get("https://www.jdpower.com/cars/shopping-guides/dimensions-and-weights-of-common-suvs").text

soup = bs(source, PARSER)

em = soup.find_all('em')
ul = soup.find_all('ul')

with open('datafile.csv', 'w') as f:
    f.write("Make/Model,Lenght (inches),Width (inches),Height (inhces),Wheelbase (inches),Curb Weight (pounds)")

counter = 0
li_counter = 4 

while True:
    try:
        with open('datafile.csv', 'a') as f:
            f.write(em[counter].text)
            f.write(',')
        for li in ul[li_counter].find_all('li'):
            num = re.findall(r'\d+', li.text)
            print(num)
            with open('datafile.csv', 'a') as f:
                f.write(str(num))
                f.write(',')
        with open('datafile.csv', 'a') as f:
            f.write('\n')
        counter += 1
        li_counter += 1

    except:
        break
