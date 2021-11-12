
import requests
#import bs4
from bs4 import BeautifulSoup
#import pandas


result = requests.get("https://r6.tracker.network/profile/pc/Beaulo.14YG/detailed")

src = result.content

soup = BeautifulSoup(src, "html.parser")

#divs = soup.find_all("div", {"class": "trn-defstat"})
divs = soup.find_all("div", {"class": "trn-card"})

dictionaies = {}
for div in divs:
    keys = []
    values = []
    name = div.find("h2", {"class": "trn-card__header-title"}).text
    both = div.find_all("div", {"class": "trn-defstat"})
    for pair in both:
        try:
            keys.append(pair.find("div", {"class": "trn-defstat__name"}).text.strip())
            values.append(pair.find("div", {"class": "trn-defstat__value"}).text.strip())
        except:
            pass      
    my_dict = dict(zip(keys, values))
    dictionaies[name] = my_dict

#trends is going to be empty


for i in dictionaies:
    print("\n\n", i, ":\n", dictionaies[i])