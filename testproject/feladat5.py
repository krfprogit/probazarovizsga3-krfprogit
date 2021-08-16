from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"
browser.get(URL)
browser.maximize_window()

varos_input = browser.find_element_by_id("missingCity")
ellenorzes_btn = browser.find_element_by_id("submit")
varosok_text = browser.find_element_by_id("cites").text
varosok_text_list = varosok_text.split(",")

for i in varosok_text_list:
    i = i.strip()
    varos_input.clear()
    varos_input.send_keys(i[1:-1])
    ellenorzes_btn.click()
    eredmeny = browser.find_element_by_id("result").text
    if eredmeny != "Nem találtad el.":
        break

assert eredmeny == "Eltaláltad."

time.sleep(2)
browser.quit()
