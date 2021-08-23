from selenium import webdriver
import time
import operator

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
browser.get(URL)
browser.maximize_window()

# input
operandus_1_input = browser.find_element_by_id('num1').text
operandus_2_input = browser.find_element_by_id('num2').text
operator_input = browser.find_element_by_id('op').text
kalkulacio_btn = browser.find_element_by_id('submit')
eredmeny = browser.find_element_by_id('result')

operandus_1_input = int(operandus_1_input)
operandus_2_input = int(operandus_2_input)
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
kalkulacio_btn.click()

szamolas = ops[operator_input](operandus_1_input, operandus_2_input)

assert str(szamolas) == eredmeny.text

time.sleep(2)
browser.quit()
