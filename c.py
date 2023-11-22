import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
codes="""
int add(int a,int b){
ret a+b;
}
"""
print("\x1bc\x1b[43;30mWait....")
driver = webdriver.Firefox()
driver.get("https://godbolt.org/")
t=True
while(t):
    elem = driver.find_element(By.XPATH,'//*[@id="alert"]')
    try:
        
        elem.send_keys(Keys.RETURN)

        t=False
    except:
        t=True

time.sleep(2)
elem = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]")
print(elem.text)
driver.close()

