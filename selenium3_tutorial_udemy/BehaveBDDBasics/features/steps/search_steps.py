import time

from behave import *


@given(u'I navigate to google.com')
def step_impl(context):

    context.driver.get("http://google.com")
    context.driver.implicitly_wait(5)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is " + title)
    assert "Googles" in title


@then(u'I enter the text as "{searchText}"')
def step_impl(context,searchText):
    context.driver.find_element_by_name("q").send_keys(searchText)


@then(u'I click the search button')
def step_impl(context):
    context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()
    time.sleep(3)
