from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"
browser.get(URL)
browser.maximize_window()

# input elemek
varos_input = browser.find_element_by_id("missingCity")
ellenorzes_btn = browser.find_element_by_id("submit")
varosok_osszes_text = browser.find_element_by_id('cites').text
varosok_random = browser.find_elements_by_xpath('//*[@id="randomCities"]/li')
eredmeny = browser.find_element_by_id('result')

varosok_osszes_list = str(varosok_osszes_text).split(', ')
varosok_osszes = []
for v in varosok_osszes_list:
    varosok_osszes.append(v.strip('"'))

varosok_random_list = []
for v in varosok_random:
    varosok_random_list.append(v.text)

for v in varosok_osszes:
    if v not in varosok_random_list:
        varos_megtalalt = v
        break

varos_input.clear()
varos_input.send_keys(varos_megtalalt)
ellenorzes_btn.click()

assert eredmeny.text == 'Eltaláltad.'

time.sleep(2)
browser.quit()
