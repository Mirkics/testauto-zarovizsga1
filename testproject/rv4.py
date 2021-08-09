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

# mezők lekérdezése

    cities = driver.find_element_by_id('cites').text
    print(cities)
    miss_city = driver.find_element_by_id("missingCity")
    check_btn = driver.find_element_by_id("submit")
    result = driver.find_element_by_id('result').text
    random_cities_list = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
    print(random_cities_list)

# kivenni egy listába a város neveket és összehasonlítani a random_cities_list elemeivel


# for i in range(len(missing_city)):
#         if cities[i] == missing_city[i]:


#   assert result == "Eltaláltad."




finally:
    driver.close()