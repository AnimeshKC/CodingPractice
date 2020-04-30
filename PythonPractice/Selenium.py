from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.wikipedia.org")

ele = driver.find_element_by_id("searchInput")
time.sleep(1)
ele.clear()
ele.send_keys("Python")
ele.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()
