'''importok'''
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


'''driver létrehozása'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/toggle.html"


# TC_001: Alap megjelenés tesztelése:
def test_01():
    driver.get(URL)
    time.sleep(2)
    felirat = driver.find_element(By.XPATH, "//h1[text()='Slide Down Toggle']")

    assert check_exists_by_xpath("//h1[normalize-space()='Slide Down Toggle']")

    open_button = driver.find_element(By.XPATH, "//label[@for='toggle']")

    assert check_exists_by_xpath("//label[@for='toggle']")


# TC_002: A toggle működtetése:
def test_02():
    driver.get(URL)
    time.sleep(2)
    open_button = driver.find_element(By.XPATH, "//label[@for='toggle']")
    open_button.click()
    time.sleep(2)
    hidden_message = driver.find_element(By.XPATH, "/html/body/div[2]/h1")
    print(hidden_message.text)
    assert check_exists_by_xpath("/html/body/div[2]/h1")

    close_button = driver.find_element(By.XPATH, "/html/body/label")
    close_button.click()

    felirat = driver.find_element(By.XPATH, "//h1[text()='Slide Down Toggle']")

    assert check_exists_by_xpath("//h1[normalize-space()='Slide Down Toggle']")

    open_button = driver.find_element(By.XPATH, "//label[@for='toggle']")

    assert check_exists_by_xpath("//label[@for='toggle']")

    driver.close()
