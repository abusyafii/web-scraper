import requests
from bs4 import BeautifulSoup as bs

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = bs(page.content, "html.parser")

print(soup)