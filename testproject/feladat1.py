from selenium import webdriver
import time


# törli majd kitölti az adott mezőt, végén gombra kattint
def input_kitolt(input_a, input_b):
    oldal_a_input.clear()
    oldal_a_input.send_keys(input_a)
    oldal_b_input.clear()
    oldal_b_input.send_keys(input_b)
    kalkulacio_btn_input.click()


# számolás eredményét adja vissza
def kalkulacio():
    eredmeny = browser.find_element_by_id('result').text
    return eredmeny


# mindent meghív, majd ellenőriz
def ellenorzes(input_a, input_b, result):
    input_kitolt(input_a, input_b)
    kalkulacio_eredmeny = kalkulacio()
    assert kalkulacio_eredmeny == result


PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
browser.get(URL)
browser.maximize_window()

# input mezők megtalálása
oldal_a_input = browser.find_element_by_id('a')
oldal_b_input = browser.find_element_by_id('b')
kalkulacio_btn_input = browser.find_element_by_id('submit')

# ellenőrzések
ellenorzes(99, 12, "222")
ellenorzes("kiskutya", 12, 'NaN')
ellenorzes('', "", 'NaN')

browser.quit()
