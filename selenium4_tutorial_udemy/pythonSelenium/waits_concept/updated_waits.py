"""
wait doc: https://www.selenium.dev/documentation/webdriver/waits/

demo example:

"""

import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')


def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"


def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"


def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"


def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda d : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"


def wait_for_element_to_be_visible(driver, element, timeout: int):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda d: element.is_displayed())
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')

def advanced_wait_for_element_to_be_visible(driver, element, timeout: int):
    try:
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda d: element.is_displayed() or True)
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')

def wait_for_element_to_be_enabled(driver, element, timeout: int):
    wait = WebDriverWait(driver, timeout)
    wait.until(lambda  d: element.is_enabled())