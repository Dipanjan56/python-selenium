import time
from typing import List, Union, Any

import pandas as pd
from numpy.random import random
import random

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def read_csv_and_fetch_creds_list(csv_file_path: str) -> list[list[Any]]:
    df = pd.read_csv(csv_file_path)
    creds_list = []

    for index, row in df.iterrows():
        username = row['username']
        password = row['password']
        creds_list.append([username, password])
    print(creds_list)
    return creds_list

def fetch_random_username_password(csv_file_path: str):
    creds_list = read_csv_and_fetch_creds_list(csv_file_path)
    random_cred = random.choice(creds_list)
    return random_cred

def wait_for_element_to_be_visible(driver, element, timeout: int):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(lambda d: element.is_displayed())
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')

def advanced_wait_for_element_for_enabled(driver, element, timeout: int, poll_frequency: float, errors: list[any]):
    try:
        wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency, ignored_exceptions=errors)
        wait.until(lambda d: element.is_enabled() or True)
    except NoSuchElementException as e:
        print(f'element not found, Exception Type: {type(e).__name__}')

def wait_for_element_to_be_enabled(driver, element, timeout: int):
    wait = WebDriverWait(driver, timeout)
    wait.until(lambda  d: element.is_enabled())


def e2e_test():
    test_url = 'https://www.saucedemo.com'
    credentials_test_data_file_path = "/Users/kdipanjan/my_projects/interview_projects/selenium_project/testdata/creds.csv"


    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'normal'
    chrome_options.headless = False

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(test_url)
    driver.maximize_window()
    time.sleep(4)

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")

    cred_list = fetch_random_username_password(credentials_test_data_file_path)

    wait_for_element_to_be_visible(driver, username, 2)
    username.send_keys(cred_list[0])
    wait_for_element_to_be_visible(driver, password, 2)
    password.send_keys(cred_list[1])
    errors = [NoSuchElementException, ElementNotInteractableException]
    advanced_wait_for_element_for_enabled(driver, login_button, 3, 0.2, errors)
    login_button.click()

    driver.quit()


if __name__ == '__main__':
    e2e_test()
