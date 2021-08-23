from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
browser.get(URL)
browser.maximize_window()

# input
operandus_1 = browser.find_element_by_id('num1').text
operandus_2 = browser.find_element_by_id('num2').text
operator = browser.find_element_by_id('op').text
kalkulacio_btn = browser.find_element_by_id('submit')
eredmeny = browser.find_element_by_id('result')

operandus_1 = int(operandus_1)
operandus_2 = int(operandus_2)
if operator == '+':
    szamolas = operandus_1 + operandus_2
elif operator == '-':
    szamolas = operandus_1 - operandus_2
elif operator == '*':
    szamolas = operandus_1 * operandus_2
else:
    szamolas = operandus_1 / operandus_2

kalkulacio_btn.click()

assert str(szamolas) == eredmeny.text

time.sleep(2)
browser.quit()
