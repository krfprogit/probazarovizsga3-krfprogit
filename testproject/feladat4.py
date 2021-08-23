from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
browser.get(URL)
browser.maximize_window()

# input
email_input = browser.find_element_by_id('email')
submit_btn = browser.find_element_by_id('submit')

# TC01: Üres
email_input.clear()
submit_btn.click()
error_message = browser.find_element_by_xpath('/html/body/div/div/form/div')

assert error_message.text == 'Kérjük, töltse ki ezt a mezőt.'
time.sleep(2)

# TC02: Helytelen
email_input.clear()
email_input.send_keys('teszt@')
submit_btn.click()

assert error_message.text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
time.sleep(2)

# TC03: Helyes kitöltés esete
email_input.clear()
email_input.send_keys('teszt@elek.hu')
submit_btn.click()

# assert not error_message.is_enabled()

time.sleep(2)
browser.quit()
