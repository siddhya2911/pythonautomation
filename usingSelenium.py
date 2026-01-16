from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d=webdriver.Edge()
d.get("https://siddhya2911.github.io/weather_app/")
time.sleep(4)
title=d.find_element(By.TAG_NAME,"h1")
titlee=d.find_element(By.TAG_NAME,"h2")
print(title.text)
print(titlee.text)
d.quit()