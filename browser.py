from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("\x1bc\x1b[43;30mbrowser")
driver = webdriver.Firefox()
driver.get("https://defuse.ca/online-x86-assembler.htm")
elem = driver.find_element(By.NAME, "instructions")
elem.send_keys("mov eax,0")
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.NAME, "submit")
elem.send_keys(Keys.RETURN)




