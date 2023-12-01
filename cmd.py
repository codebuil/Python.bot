import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


text="""
mov eax,0
mov ebx,0
mov ecx,0
mov edx,0
mov esi,0
mov edi,0

"""
print("\x1bc\x1b[43;30mWait....")
driver = webdriver.Firefox()
driver.get("https://defuse.ca/online-x86-assembler.htm")
elem = driver.find_element(By.NAME, "instructions")
elem.send_keys(text)
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.NAME, "submit")
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
#/html/body/div[1]/div[3]/div[2]/div[2]/p[2]

elem = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/p")
for n in elem:
    print(n.text)
driver.close()

