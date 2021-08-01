
from bs4 import BeautifulSoup as bs
import requests

PARSER = 'html.parser'

source = requests.get("https://coreyms.com").text

soup = bs(source, PARSER)

for article in soup.find_all('article'):    
    print(article.header.h2.a.text.upper())
    print(article.div.p.text)
    print()

