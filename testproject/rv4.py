## 5 Feladat: Kakukktojás - városok

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    # Oldal betöltése
    driver.get('https://black-moss-0a0440e03.azurestaticapps.net/rv4.html')
    time.sleep(2)

    cities_list = driver.find_element_by_xpath('//*[@id="cites"]/text()')
    print(cities_list)


finally:
    driver.close()