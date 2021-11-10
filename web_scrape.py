import lxml
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#initiate web driver + install the chrome driver if it does not exist
driver = webdriver.Chrome(ChromeDriverManager().install())

def scrape_page(url):
    """
    Function to scrape the page:
        -checks if the page is vaild first and  if so it will load the page
        -click 'ok' on the accept cookies message
        -grabs the current property name
        -clicks on the 'Show all N Amenities
        -initiates beautiful soup
    returns the property name and the beautiful soup object
    """
    driver.get(url)
    #introduce a small delay so the page can fully load
    time.sleep(7)

    if not check_url(url):

        driver.maximize_window()

        #accept cookies
        accept_cookies_button = find_button_to_click("/html/body/div[5]/div/div/div[1]/div/div[2]/section/div[2]/div[2]/button")
        click_button(accept_cookies_button)

        property_name = driver.find_elements_by_xpath("//*/h2[@class='_14i3z6h']")[0].text

        show_all_amenities = find_button_to_click("//*[contains(text(), 'Show all')]", index=1)
        click_button(show_all_amenities)

        soup = BeautifulSoup(driver.page_source, "lxml")

        return property_name, soup

    else:
        soup = BeautifulSoup()
        return "Undefined", url



def check_url(url: str) -> bool:
    """
    Function to check if the url provided is valid
        -tries to scrape the page for the error message (403)
        and if found returns False (meaning it's not a valid page)
        else returns true
    """
    try:
        potential_error = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div/div/section/div[2]/div").text
        if '403' in potential_error:
            return True
    except:
        return False

def find_button_to_click(xpath: str, index=None):
    try:
        if index is not None:
            button = driver.find_elements_by_xpath(xpath)[index]
        else: button = driver.find_element_by_xpath(xpath)
        return button
    except:
        pass


def click_button(button_to_click):
    """
    Tries to click the giving button, using 
    try/except for error catching
    """
    try:
        button_to_click.click()
    except:
        print("Button not found")

def find_amenities(xpath: str) -> list:
    """
    Scrpaes the amenities for the web page 
    given the xpath. Returns a list
    """
    amenities = driver.find_elements_by_xpath(xpath)
    return [amenitie.text for amenitie in amenities]

def find_data_in_soup(soup, tag: str, class_id:str) -> str:
    """
    Returns the text of a given tag / class id
    within a Beautiful Soup objhect()
    """
    return soup.find(tag, class_=class_id).get_text()

def kill_window():
    """Terminate broswer window"""
    driver.quit()