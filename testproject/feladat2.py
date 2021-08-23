from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
browser.get(URL)
browser.maximize_window()

# input
penzfeldobas_btn = browser.find_element_by_id('submit')
utolso_eredmeny = browser.find_element_by_id('lastResult')
penzfeldobas_fej_db = 0

for i in range(100):
    penzfeldobas_btn.click()
    if utolso_eredmeny.text == "fej":
        penzfeldobas_fej_db += 1

assert penzfeldobas_fej_db >= 30

time.sleep(1)
browser.quit()
