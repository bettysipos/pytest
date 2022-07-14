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
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/calculator.html"
driver.get(URL)
time.sleep(2)

# TC_001: Áfa és bruttó összeg számítás árucikkek vásárlásakor:

def test_1():
    # 1000
    button_1 = driver.find_element(By.XPATH, '//button[text()="1"]')
    button_1.click()
    button_0 = driver.find_element(By.XPATH, '//button[text()="0"]')
    button_0.click()
    button_0.click()
    button_0.click()

    # +
    button_add = driver.find_element(By.XPATH, '//button[text()="+"]')
    button_add.click()

    # 3000
    button_3 = driver.find_element(By.XPATH, '//button[text()="3"]')
    button_3.click()
    button_0.click()
    button_0.click()
    button_0.click()
    button_equal = driver.find_element(By.XPATH, "//button[normalize-space()='=']")
    button_equal.click()


    # kijelző
    kijelzo = driver.find_element(By.XPATH, '//div[@class="auto-scaling-text"]')
    print(kijelzo.text)

    assert kijelzo.text == '4 000'

    # szorzás
    szorzas = driver.find_element(By.XPATH, '//button[text()="×"]')
    szorzas.click()

    # 27
    button_2 = driver.find_element(By.XPATH, '//button[text()="2"]')
    button_2.click()
    button_7 = driver.find_element(By.XPATH, '//button[text()="7"]')
    button_7.click()

    # %
    button_percent = driver.find_element(By.XPATH, "//button[normalize-space()='%']")
    button_percent.click()

    # =
    button_equal.click()

    # kijelző
    kijelzo = driver.find_element(By.XPATH, '//div[@class="auto-scaling-text"]')
    print(kijelzo.text)

    assert kijelzo.text == '1 080'

    # +
    button_add.click()


    # 4000
    button_4 = driver.find_element(By.XPATH, '//button[text()="4"]')
    button_4.click()
    button_0.click()
    button_0.click()
    button_0.click()
    # =
    button_equal.click()

    kijelzo = driver.find_element(By.XPATH, '//div[@class="auto-scaling-text"]')
    print(kijelzo.text)

    assert kijelzo.text == '5 080'

    driver.close()