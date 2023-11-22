import time 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("\x1bc\x1b[43;30mWait....")
driver = webdriver.Firefox()
driver.get("https://defuse.ca/online-x86-assembler.htm")
elem = driver.find_element(By.NAME, "instructions")
elem.send_keys("mov eax,0")
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.NAME, "submit")
elem.send_keys(Keys.RETURN)
time.sleep(2)
#/html/body/div[1]/div[3]/div[2]/div[2]/p[2]

elem = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/p")
for n in elem:
    print(n.text)
driver.close()

