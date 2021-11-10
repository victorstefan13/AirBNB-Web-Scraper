
"""
Initial Prototype to get an idea of how this can be implemented
"""

import lxml
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.airbnb.co.uk/rooms/20669368"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()
time.sleep(10)
accept_cookies = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/section/div[2]/div[2]/button")
property_name = driver.find_elements_by_xpath("//*/h2[@class='_14i3z6h']")[0].text
accept_cookies.click()
amenities_location = driver.find_elements_by_xpath("//*[contains(text(), 'What this place offers')]")[0]
button = driver.find_elements_by_xpath("//*[contains(text(), 'Show all')]")[1]

try:
    button.click()
except:
    print("CANNOT FIND BUTTON!!!")

soup = BeautifulSoup(driver.page_source, "lxml")

property_type = soup.find("div", class_="_1qsawv5").get_text()
property_details = wsh.split_str(soup.find("ol", class_="_194e2vt2").get_text())

amenities = driver.find_elements_by_xpath("//*[@class='_gw4xx4']")

amenities_data = [amenitie.text for amenitie in amenities]

driver.quit()