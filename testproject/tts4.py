# 2. feladat: pénzfeldobás app. Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
#
# Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/tts4.html')
    time.sleep(2)

    submit_button = driver.find_element_by_id('submit')

    # gomb megnyomása 100.szor. megszámolni a 'fej' elemeket. Ha talál egyet, akkor növekszik a dbszám egyel.
    number_fej = 0
    for i in range(1, 100):
        submit_button.click()
        #time.sleep(1)
        result = driver.find_element_by_id('lastResult').text
        if result == 'fej':
            number_fej += 1

# minimum 30 db fej kell
    assert number_fej >= 30


finally:
    driver.close()
