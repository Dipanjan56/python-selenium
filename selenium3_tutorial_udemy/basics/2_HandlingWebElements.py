import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

# username = driver.find_element_by_id("identifierId")
# username.send_keys("trainer@way2automation.com")


driver.find_element(by=By.ID, value="identifierId").send_keys("trainer@way2automation.com")
time.sleep(60)
# driver.find_element(by=By.XPATH, value="//*[@id=\"identifierNext\"]/div/button/div[2]").click()
#
# element = wait.until(
#     EC.element_to_be_clickable((By.XPATH,"//*[@id=\"password\"]/div[1]/div/div[1]/input")))
#
# element.send_keys("ksfbksndfsjkdfj")
#
# driver.find_element(by=By.XPATH, value="//*[@id=\"passwordNext\"]/div/button/div[2]").click()
#
# error_msg = driver.find_element(by=By.XPATH, value="//*[@id=\"view_container\"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]").text
# print(error_msg)