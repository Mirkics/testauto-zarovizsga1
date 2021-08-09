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

    number_a = int(driver.find_element_by_id('num1').text)
    print(number_a)

    number_b = int(driver.find_element_by_id('num2').text)
    print(number_b)

    operandus = driver.find_element_by_id('op').text
    submit_btn = driver.find_element_by_id('submit')
    submit_btn.click()

    time.sleep(2)
    result = driver.find_element_by_id('result').text

    if operandus == "+":
        result_plus = (number_a + number_b)

        assert result == result_plus

    if operandus == "-":
        result_minus = (number_a - number_b)

        assert result == result_minus

    if operandus == "+":
        result_multp = (number_a * number_b)

        assert result == result_multp
    if operandus == "/":
        result_div = (number_a / number_b)

        assert result == result_div
    else:
        pass

finally:
    driver.close()
