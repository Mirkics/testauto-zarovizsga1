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

finally:
    driver.close()