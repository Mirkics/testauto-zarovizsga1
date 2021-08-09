# téglalap kerülete app

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

    input_a = driver.find_element_by_id("a")
    input_b = driver.find_element_by_id("b")

    calc_button = driver.find_element_by_id("submit")

    #result = driver.find_element_by_id("result")
    result = driver.find_element_by_xpath('//*[@id="result"]')


    # * Helyes kitöltés esete:
    #     * a: 99
    #     * b: 12
    #     * Eredmény: 222

    input_a.send_keys('99')
    input_b.send_keys('12')
    time.sleep(2)
    calc_button.click()
    print(result)

    #assert result == "222"

    input_a.clear()
    input_b.clear()
    time.sleep(2)
#
# * Nem számokkal történő kitöltés:
#     * a: kiskutya
#     * b: 12
#     * Eredmény: NaN
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * Eredmény: NaN

finally:
    driver.close()
