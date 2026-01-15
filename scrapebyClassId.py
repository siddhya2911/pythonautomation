# import requests
# from bs4 import BeautifulSoup
# import time

# url = "https://www.amazon.in/"
# soup = BeautifulSoup(requests.get(url).text, "html.parser")

# # By class
# content = soup.find("div", class_="a-carousel-card")
# print(a-carousel-card.text)

# # By id
# section = soup.find(id="main")
# print(section.text)

import requests
from bs4 import BeautifulSoup
import time
url = "https://www.amazon.in/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    print(link.get("href"))

time.sleep(6)