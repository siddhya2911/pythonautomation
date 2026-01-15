from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d=webdriver.Edge()
d.get("https://www.flipkart.com/")
time.sleep(4)
title=d.find_element(By.TAG_NAME,"h2")
print(title.text)
d.quit()