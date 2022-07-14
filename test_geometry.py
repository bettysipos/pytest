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

'''driver létrehozása'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/geometry.html"


# TC_001: Alapállapot tesztelése:
def test_01():
    driver.get(URL)
    time.sleep(2)
    alap = driver.find_element(By.ID, 'a')
    print(alap.get_attribute('value'))
    assert alap.get_attribute('value') == ''

    magassag = driver.find_element(By.ID, 'm')
    print(magassag.get_attribute('value'))
    assert magassag.get_attribute('value') == ''

    results = driver.find_element(By.ID, 'results')
    assert not results.is_displayed()


# TC_002: Háromszög területének kiszámítása (alap * magasság / 2)
def test_02():
    driver.get(URL)
    time.sleep(2)
    alap = driver.find_element(By.ID, 'a')
    alap.send_keys('5')
    time.sleep(1)
    magassag = driver.find_element(By.ID, 'm')
    magassag.send_keys('4')

    gomb_haromszog_terulete = driver.find_element(By.ID, 'submitT')
    gomb_haromszog_terulete.click()

    results_haromszog = driver.find_element(By.XPATH, '//div[@id="results"]//p[1]')
    print(results_haromszog.text)

    assert results_haromszog.text == 'Háromszög területe: 10.00'

    results_rombusz = driver.find_element(By.XPATH, '//div[@id="results"]//p[2]')
    print(results_rombusz.text)

    assert results_rombusz.text == 'Rombusz területe:'


# TC_003: Háromszög és rombusz területének kiszámítása (alap * magasság / 2, alap * magasság)
def test_03():
    driver.get(URL)
    time.sleep(2)
    alap = driver.find_element(By.ID, 'a')
    alap.send_keys('7')
    time.sleep(1)
    magassag = driver.find_element(By.ID, 'm')
    magassag.send_keys('5')

    gomb_haromszog_terulete = driver.find_element(By.ID, 'submitT')
    gomb_haromszog_terulete.click()

    gomb_rombusz_terulet = driver.find_element(By.ID, 'submitD')
    gomb_rombusz_terulet.click()

    results_haromszog = driver.find_element(By.XPATH, '//div[@id="results"]//p[1]')
    print(results_haromszog.text)

    assert results_haromszog.text == 'Háromszög területe: 17.50'

    results_rombusz = driver.find_element(By.XPATH, '//div[@id="results"]//p[2]')
    print(results_rombusz.text)

    assert results_rombusz.text == 'Rombusz területe: 35'

    driver.close()
