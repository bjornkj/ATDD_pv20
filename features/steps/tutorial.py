import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from blender import Blender


@given("webbrowser open on google")
def step_impl(context):
    browser = context.browser
    browser.get("https://www.google.com")


@when("we search for the term kyh")
def step_impl(context):
    browser = context.browser
    # få tag i sökfältet
    browser.find_element(By.XPATH, '//*[@id="L2AGLb"]/div').click()

    search_field = browser.find_element(By.NAME, "q")
    search_field.send_keys("kyh")
    search_field.send_keys(Keys.ENTER)
    time.sleep(20)
    # Skicka tangenttryck/text till sökfältet
    # Skicka <enterslag>


@given('I put {thing} in a blender')
def step_impl(context, thing):
    context.blender = Blender()
    context.blender.add(thing)


@when('I switch the blender on')
def step_impl(context):
    context.blender.switch_on()


@then('it should transform into {resulting_thing}')
def step_impl(context, resulting_thing):
    assert context.blender.result == resulting_thing, f"Expected {resulting_thing} got {context.blender.result}"


@given("I am on the todo page")
def step_impl(context):
    context.browser.get("https://lambdatest.github.io/sample-todo-app/")

@when("I click done on all todos")
def step_impl(context):
    for element in context.browser.find_elements(By.XPATH, "//ul/li"):
        element.find_element(By.XPATH, "input").click()


@then(u'Remaining todos should be 0')
def step_impl(context):
    remaining_text = context.browser.find_element(By.CSS_SELECTOR, ".ng-binding").text
    remaining = int(remaining_text.split()[0]) # remaining text looks like 0 of 5 remaining, get the first number as int
    assert remaining == 0, f"'{remaining}' remain todos, expected 0"
