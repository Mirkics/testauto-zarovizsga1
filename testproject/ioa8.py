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

finally:
    driver.close()