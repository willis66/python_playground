from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()
digitalscout = (
    "https://stats.digitalscout.com/football/boys/game/13959041"  # Only needs Beaverton
)
r = s.get(digitalscout)

soup = BeautifulSoup(r.content, "html.parser")
main = soup.find_all("div", class_="content")
for i in main:
    print(i.prettify())
