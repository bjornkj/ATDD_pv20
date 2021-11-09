import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
