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


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


'''driver létrehozása'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/rock_paper_scissors.html"


# TC_001: Betöltés utáni állapot tesztelése
def test_01():
    driver.get(URL)
    time.sleep(2)
    wins = driver.find_element(By.XPATH, "//div[@class='win']//span")
    assert wins.text == '0'
    tie = driver.find_element(By.XPATH, "//div[@class='tie']//span")
    assert tie.text == '0'
    loss = driver.find_element(By.XPATH, "//div[@class='loss']//span")
    assert loss.text == '0'
    total = driver.find_element(By.XPATH, "//div[@class='move']//span")
    assert total.text == '0'


# TC_002: Működés megfelelősége:
def test_02():

    driver.get(URL)
    time.sleep(2)
    rock = driver.find_element(By.ID, 'rock')
    rock.click()
    time.sleep(2)
    cpu = driver.find_element(By.XPATH, '//body//aside//i[2]')
    print(cpu.get_attribute('class'))
    if cpu.get_attribute('class') == "fa fa-hand-rock-o":
        wins = driver.find_element(By.XPATH, "//div[@class='win']//span")
        assert wins.text == '0'
        tie = driver.find_element(By.XPATH, "//div[@class='tie']//span")
        assert tie.text == '1'
        loss = driver.find_element(By.XPATH, "//div[@class='loss']//span")
        assert loss.text == '0'
        total = driver.find_element(By.XPATH, "//div[@class='move']//span")
        assert total.text == '1'

    if cpu.get_attribute('class') == "fa fa-hand-paper-o":
        wins = driver.find_element(By.XPATH, "//div[@class='win']//span")
        assert wins.text == '0'
        tie = driver.find_element(By.XPATH, "//div[@class='tie']//span")
        assert tie.text == '0'
        loss = driver.find_element(By.XPATH, "//div[@class='loss']//span")
        assert loss.text == '1'
        total = driver.find_element(By.XPATH, "//div[@class='move']//span")
        assert total.text == '1'

    if cpu.get_attribute('class') == 'fa fa-hand-scissors-o':
        wins = driver.find_element(By.XPATH, "//div[@class='win']//span")
        assert wins.text == '1'
        tie = driver.find_element(By.XPATH, "//div[@class='tie']//span")
        assert tie.text == '0'
        loss = driver.find_element(By.XPATH, "//div[@class='loss']//span")
        assert loss.text == '0'
        total = driver.find_element(By.XPATH, "//div[@class='move']//span")
        assert total.text == '1'


# TC_003: Frissitsük az oldalt és hajtsunk végre 5 játékot :
def test_03():
    driver.get(URL)
    time.sleep(2)

    rock = driver.find_element(By.ID, 'rock')
    paper = driver.find_element(By.ID, 'paper')
    scissors = driver.find_element(By.ID, 'scissors')

    lehet = [rock, paper, scissors]

    for i in range(5):
        random.choice(lehet).click()

    time.sleep(2)

    history = driver.find_elements(By.XPATH, "//body//aside//div[starts-with(@class,'history-item')]")
    assert len(history) == 5

    driver.close()
