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
import random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/stopwatch.html"


# TC_001: Alkalmazás alaphelyzetének tesztelése:
def test_01():
    driver.get(URL)
    time.sleep(2)
    stopwatch = driver.find_element(By.XPATH, "//div[@class='stopwatch']")
    print(stopwatch.text)
    assert stopwatch.text == '00: 00: 00'

    start_button = driver.find_element(By.XPATH, "//a[@id='start']")
    start_button.click()

    time.sleep(2)
    driver.get(URL)
    time.sleep(2)
    stopwatch = driver.find_element(By.XPATH, "//div[@class='stopwatch']")
    print(stopwatch.text)
    assert stopwatch.text == '00: 00: 00'


# TC_002: Megállítás x másodpercnél:
def test_02():
    driver.get(URL)
    time.sleep(2)
    start_button = driver.find_element(By.XPATH, "//a[@id='start']")
    start_button.click()
    time.sleep(5)
    stop_button = driver.find_element(By.XPATH, "//a[@id='stop']")
    stop_button.click()

    stopwatch = driver.find_element(By.XPATH, "//div[@class='stopwatch']")
    print(stopwatch.text)
    masodperc = stopwatch.text.split(': ')[1]
    print(int(masodperc))

    assert int(masodperc) >= 4 and int(masodperc) <= 6


# TC_003: Lapszámláló tesztelése:
def test_03():
    driver.get(URL)
    time.sleep(2)
    start_button = driver.find_element(By.XPATH, "//a[@id='start']")
    start_button.click()
    time.sleep(5)
    stop_button = driver.find_element(By.XPATH, "//a[@id='stop']")
    stop_button.click()
    lap_button = driver.find_element(By.XPATH, "//a[@id='lap']")
    lap_button.click()

    stopwatch = driver.find_element(By.XPATH, "//div[@class='stopwatch']")
    print(stopwatch.text)

    lapwatch = driver.find_element(By.XPATH, '//li')
    print(lapwatch.text)

    assert stopwatch.text == lapwatch.text
    driver.close()
