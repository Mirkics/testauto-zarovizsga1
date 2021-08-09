# 3 Feladat: Összeadó.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html')
    time.sleep(2)

    number_a = driver.find_element_by_id('num1').text
    print(number_a)
    number_b = driver.find_element_by_id('num2').text
    print(number_b)
    operandus = driver.find_element_by_id('op')
    submit_btn = driver.find_element_by_id('submit')
    submit_btn.click()

    time.sleep(2)

    result = driver.find_element_by_id('result')

    print(result)

    #assert ==

finally:
    driver.close()