from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("\x1bc\x1b[43;30mbrowser")
driver = webdriver.Firefox()
driver.get("https://github.com/codebuil?tab=repositories")

