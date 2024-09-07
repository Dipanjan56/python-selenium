"""Locators"""

"""

doc: https://www.selenium.dev/documentation/webdriver/elements/locators/


Types of locators:
1. id
2. name
3. cssSelector
4. xpath
5. tagName
6. className
7. linkText
8. partialLinkText
"""

"""Best tool to use: 
"""

"""
Xpath: there are 3 types -> absolute xpath, relative xpath, partial xpath

element of the page:

<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0" 
aria-label="Email or phone" name="identifier" value="" autocapitalize="none" id="identifierId" dir="ltr" 
data-initial-dir="ltr" data-initial-value="trainer@way2automation.com" badinput="false">

#------------------------------------------------------------------

Relative xpath:

basic syntax of xpath: //tagName[@attribute='value'] -> this is called relative x-path as it is created using the attribute
e.g -> //input[@id='identifierId'] 

also we can concatenate other attributes as well to select the element more precisely
e.g //input[@id='identifierId'][@name='identifier'] 
                        or 
//input[@id='identifierId' and @name='identifier']

if you want to verify the same in console -> use this $x 
paste this code -> $x("//input[@id='identifierId']")

if we paste like $x("//*") here * means any tag in the page

#------
 now lets say there are two elements using this xpath no matter how many attributes we concatenate
 then we can solve it like these:
 1. using indexes -> (//input[@id='identifierId'][@name='identifier'])[0]
 2. using parent sibling approach

#-------

Dynamic Xpath: 

For Dynamic element: when a element keeps on changing everytime page loads
1. if prefix is dynamic and postfix is constant-> //input[starts-with(@id,'iden')]
2. if prefix is constant and postfix is dynamic -> //input[ends-with(@id,'fierId')]
3. if only middle part is constant -> //input[contains(@id,'iden')]
4. using parent child concept: 
    1. if we want to go to parent of this element-> 
    //input[@id='identifierId']/..
            or
    //input[@id='identifierId']/parent::div 

    2. if we want to go to child of this element ->
    //div[@class='aXBtI Wic03c']/div
    3. if we want to go to second child ->
    //div[@class='aXBtI Wic03c']/div[2]

    3. if we want to go to above sibling from another preceding child [sibling] ->
    //div[@class='aXBtI Wic03c']/div[3]/preceding-sibling::div
    it will give us all the preceding sibling, if we want just the above sibling
    //div[@class='aXBtI Wic03c']/div[3]/preceding-sibling::div[1]
                                or
    //div[@class='aXBtI Wic03c']/div[3]/preceding-sibling::div[@jsname='Xnnbs'] -> for particular sibling

    3. if we want to go to below sibling from another child [following sibling] ->
    it will give us all the preceding sibling, if we want just the below sibling
    //div[@class='aXBtI Wic03c']/div[3]/following-sibling::div[1]
                                or
    //div[@class='aXBtI Wic03c']/div[3]/following-sibling::div[@jsname='Xnnbs'] -> for particular sibling


4. if we dont know tagName or anything but lets say just the text -->
    1. for partial text: //*[contains(text(),'SignIn')]   
    2. for full text: //*[text()='Signin']


#------------------------------------------------------------------

Absolute X-path:
This always starts from root dir i.e from //html   

e.g. //html/body/div[1]/div[1]/content/div[2]/div[2]/div/div[1]/div[2]/form/content/div[1]/.... and so on


#------------------------------------------------------------------


Partial X-path:
remove as much prefix as needed from absolute xpath
e.g. /content/div[2]/div[2]/div/div[1]/div[2]/form/content/div[1]


we can also have auto-generated x-path from chrome
Steps:
go to inspect element -> in developer tools go to Elements section -> go to the specific element -> right click on it->
click on copy -> click on copy x-path 

e.g.//*[@id="identifierId"]


#------------------------------------------------------------------
"""

"""
CSS Selector:

one disadvantage is in css, we can only move forward/downward as there is no concept like preceding sibling in css
but css is faster than xpath
also we cant locate an element based on text in css

element of the page:

<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0" 
aria-label="Email or phone" name="identifier" value="" autocapitalize="none" id="identifierId" dir="ltr" 
data-initial-dir="ltr" data-initial-value="trainer@way2automation.com" badinput="false">

basic syntax -> tagName[attribute='value']
e.g. input[id='identifierId']

if you want to verify the same in console -> use this $$ 
paste this code -> $$("input[id='identifierId']")

also we can concatenate other attributes as well to select the element more precisely
e.g input[id='identifierId'][name='identifier']
    div[role='presentation']

#----------------------------------------

Dynamic CSS:
For Dynamic element: when a element keeps on changing everytime page loads
1. if postfix is dynamic -> input[id^='iden']
2. if prefix is constant and postfix is dynamic -> input[id$='fierId']
3. if only middle part is constant -> input[id*='fier']
4. using parent child concept: 
    1. using > (for direct child): e.g. div .whsOnd > div > div     -> it will give us all the children 
    2. if we want only first-child: div .whsOnd > div > div:first-child
    3. if we want only last-child: div .whsOnd > div > div:last-child
    4. if we want only third-child: div .whsOnd > div > div:nth-child(3)


#----------------------------------------

For id:
use #
e.g. #identifierId

For tagName:
use tagName only
e.g input

mixn'match both tagName and id: 
use tagName#id
e.g. input#identifierId

For class:
use .
e.g. .Xb9hP

if className is like this: class="whsOnd zHQkBf"
then use . in every space
e.g. ->  .whsOnd.zHQkBf

concatenate any attribute in css:
e.g. -> input#identifierId.whsOnd.asdasjhh[type='email']


#----------------------------------------

"""

"""
Complex Elements:

if we cant find element as its getting vanishing from the page once we want to inspect that element,
then use selectorsHub tool and click on 'Turn On debugger on the bottom right tab on the selectorsHub Menu
and then do the prerequisite steps and then click on inspect button and then click on the element

"""



from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/rahulshetty/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()















