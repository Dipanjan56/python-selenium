from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()


#chrome_options = webdriver.ChromeOptions()
# notification preferences: 1 for allow, 2 for disallow
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# if you want to run it in headless mode
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

driver.get("http://www.google.com")
driver.maximize_window()

print(driver.title)