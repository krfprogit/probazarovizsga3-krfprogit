from selenium import webdriver
import time


def input_kitolt(a, b):
    oldal_a_input.clear()
    oldal_a_input.send_keys(a)
    oldal_b_input.clear()
    oldal_b_input.send_keys(b)
    kalkulacio_btn_input.click()


def kalkulacio():
    eredmeny = browser.find_element_by_id('result').text
    return eredmeny


PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
browser.get(URL)
browser.maximize_window()

# input mezők megtalálása
oldal_a_input = browser.find_element_by_id('a')
oldal_b_input = browser.find_element_by_id('b')
kalkulacio_btn_input = browser.find_element_by_id('submit')

# input mezők kitöltése_1
input_kitolt(99, 12)
# eredmény kiolvasása_1
kalkulacio_eredmeny = kalkulacio()
# ellenőrzés_1
assert kalkulacio_eredmeny == "222"

# kalkuláció_2
input_kitolt("kiskutya", 12)
kalkulacio_eredmeny = kalkulacio()
assert kalkulacio_eredmeny == 'NaN'

# kalkuláció_3
input_kitolt('', '')
kalkulacio_eredmeny = kalkulacio()
assert kalkulacio_eredmeny == 'NaN'

browser.quit()
