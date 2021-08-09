# 1. feladat: téglalap kerülete app

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/x234.html')
    time.sleep(2)

    # Tesztadatok
    data_a = ["99", "kiskutya", ""]
    data_b = ["12", "12", ""]
    expected_result = ["222", "NaN", "NaN"]

    input_a = driver.find_element_by_id("a")
    input_a.get_attribute('value')
    input_b = driver.find_element_by_id("b")
    input_b.get_attribute('value')
    calc_button = driver.find_element_by_id("submit")

    #result = driver.find_element_by_id("result")

    result = driver.find_element_by_xpath('//*[@id="result"]')

    # * Helyes kitöltés esete:
    #     * a: 99
    #     * b: 12
    #     * Eredmény: 222

    input_a.send_keys(data_a[0])
    input_b.send_keys(data_b[0])
    time.sleep(2)
    calc_button.click()
    print(result.text)

    assert result.text == expected_result[0]


    input_a.clear()
    input_b.clear()
    time.sleep(2)
#
# * Nem számokkal történő kitöltés:
#     * a: kiskutya
#     * b: 12
#     * Eredmény: NaN

    input_a.send_keys(data_a[1])
    input_b.send_keys(data_b[1])
    time.sleep(2)
    calc_button.click()
    print(result.text)

    assert result.text == expected_result[1]


    input_a.clear()
    input_b.clear()
    time.sleep(2)
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * Eredmény: NaN

    input_a.send_keys(data_a[2])
    input_b.send_keys(data_b[2])
    time.sleep(2)
    calc_button.click()
    print(result.text)

    assert result.text == expected_result[2]

finally:
    driver.close()
