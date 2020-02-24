import lxml
import requests
from bs4 import BeautifulSoup


url = "https://www.instagram.com/{}/"


def scrape(USRNME):
    full_url = url.format(USRNME)
    r = requests.get(full_url)
    s = BeautifulSoup(r.text, "lxml")

    tag = s.find("meta", attrs={"name": "description"})
    text = tag.attrs['content']
    main_text = text.split("-")[0]

    return main_text


USRNME = "mycherrycrush"
data = scrape(USRNME)

print(data)
