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

    result = driver.find_elements_by_id('//*[@id="results"]')

    # gomb megnyomása 100.szor. Az eredményt kiírni egylistába és megszámolni a listában lévő 'fej' elemeket.

    for i in range(100):
        submit_button.click()
        #count['fej']


    time.sleep(10)

finally:
    driver.close()
