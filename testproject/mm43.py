## 4 Feladat: Email mező * Helyes kitöltés esete:
#     * email: teszt@elek.hu
#     * Nincs validációs hibazüzenet
#
# * Helytelen:
#     * email: teszt@
#     * Please enter a part following '@'. 'teszt@' is incomplete.
#
# * Üres:
#     * email: <üres>
#     * b: <üres>
#     * Please fill out this field.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/mm43.html')
    time.sleep(2)

    input_email = driver.find_element_by_id('email')
    btn_submit = driver.find_element_by_id('submit')
# tc 1:
    input_email.send_keys("teszt@elek.hu")
    btn_submit.click()

    #assert input_email == "teszt@elek.hu"

    input_email.clear()
    time.sleep(2)

# Tc2

    input_email.send_keys("teszt@")
    btn_submit.click()
    message = driver.find_element_by_xpath('/html/body/div/div/form/div').text
    print(message)

    assert message == "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    input_email.clear()
    time.sleep(2)

# tc3
    btn_submit.click()
    message = driver.find_element_by_xpath('/html/body/div/div/form/div').text
    print(message)

    assert message == "Kérjük, töltse ki ezt a mezőt."

finally:
    driver.close()