from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
browser.get(URL)
browser.maximize_window()

# input mezők megtalálása
oldal_a_input = browser.find_element_by_id('a')
oldal_b_input = browser.find_element_by_id('b')
kalkulacio_btn_input = browser.find_element_by_id('submit')

# input mezők kitöltése
oldal_a_input.send_keys('99')
oldal_b_input.send_keys('12')
kalkulacio_btn_input.click()

# eredmény kiolvasása
kalkulacio_eredmeny = int(browser.find_element_by_id('result').text)

# ellenőrzés
assert kalkulacio_eredmeny == 222

browser.quit()
