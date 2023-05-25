import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


def wait_for_element_to_be_visible(driver, locator_name: str, locator_value: str, time_in_seconds: int):
    global element
    try:
        if str(locator_name).endswith('ID'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.ID, locator_value)))
        elif str(locator_name).endswith('XPATH'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.XPATH, locator_value)))
        elif str(locator_name).endswith('CSS'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator_value)))
        elif str(locator_name).endswith('NAME'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.NAME, locator_value)))
        elif str(locator_name).endswith('TAG_NAME'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.TAG_NAME, locator_value)))
        elif str(locator_name).endswith('CLASS_NAME'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif str(locator_name).endswith('LINK_TEXT'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
            element = WebDriverWait(driver, time_in_seconds).until(
                EC.visibility_of_element_located(
                    (By.PARTIAL_LINK_TEXT, locator_value)))
        print(f'element: {element.text} is found successfully')
    except NoSuchElementException as e:
        print(
            f"Not able to get element | locator_name: {locator_name} | locator_value: {locator_value} | Exception Type: {type(e).__name__}")
    except TimeoutException:
        print(
            f"TIME OUT ERROR Occurred! Element not visible | locator_name: {locator_name} | locator_value: {locator_value} | wait_time: {time_in_seconds} seconds")
    except Exception as e:
        print(
            f"Exception Occurred! | locator_name: {locator_name} | locator_value: {locator_value} | wait_time: {time_in_seconds}")
        print(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")
    return element

chrome_options = ChromeOptions()
chrome_options.headless = False

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

driver.get('https://www.saucedemo.com/')

username = wait_for_element_to_be_visible(driver, 'username_ID', 'user-name', 5)
password = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'password')))

username.send_keys('standard_user')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

time.sleep(5)

inventory_item_list = driver.find_elements(By.CSS_SELECTOR, '.inventory_list .inventory_item')
for item in inventory_item_list:
    print(item.find_element(By.CLASS_NAME, 'inventory_item_name').text)

driver.quit()
