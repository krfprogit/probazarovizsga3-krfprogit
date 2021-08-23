from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
browser.get(URL)
browser.maximize_window()

# time.sleep(2)
# browser.quit()
