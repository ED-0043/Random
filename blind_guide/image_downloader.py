import os
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = Firefox()
browser.get("https://google.com")

search = browser.find_element(By.CLASS_NAME,".YacQv" )
search.click()
search.send_keys("sign for speak")




