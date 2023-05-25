from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# service_obj = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_obj, options=options)

# options = webdriver.FirefoxOptions()
# service_obj = FirefoxService(executable_path=GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service_obj, options=options)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()









