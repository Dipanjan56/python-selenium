import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
# English - US English - UK

dropdown = driver.find_element(by=By.ID, value="searchLanguage")
select = Select(dropdown)
#select.select_by_visible_text("Eesti")
select.select_by_value("hi")

options = dropdown.find_elements(by=By.TAG_NAME, value="option")

for option in options:
    print("Text is : ",option.text, "Lang is : "+option.get_attribute("lang"))


print("Total dropdown values are ",len(options))


print("----------Printing all links--------------")

block = driver.find_element(by=By.XPATH, value="//*[@id=\"www-wikipedia-org\"]/div[7]/div[3]")

links = block.find_elements(by=By.TAG_NAME, value="a")

print("1st link is : ",block.find_element(by=By.TAG_NAME, value="a").__getitem__(0).text)
#block2.find_elements_by_tag_name("abc").__getitem__(2).click()
print(len(links))

for link in links:
    print("Text is : ",link.text," ---URL is : "+link.get_attribute("href"))