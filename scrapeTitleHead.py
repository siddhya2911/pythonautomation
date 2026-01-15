import requests
from bs4 import BeautifulSoup

url = "https://siddhya2911.github.io/weather_app/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Page title
print("Title:", soup.title.text)

# All headings
for h in soup.find_all("h1"):
    print("H1:", h.text)
