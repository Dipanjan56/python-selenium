"""Allure Reporting"""


"""

Steps to configure
1. got to google and search 'download allure command line'
2. go to allure reporting website: https://docs.qameta.io/allure/
3. brew install allure
4. also install python based lib -> allure-pytest~=2.12.0 [requirements.txt]
5. In order to do allure report -> you have to run tests first and save json reports in a dir e.g. allurereports
6. Then allure report gets feeded from the json files and creates an html report for user

terminal -> 
1. pytest test_webdriver_integration.py -s -v --alluredir="./allurerports"
2. allure serve ./allurereports

"""

