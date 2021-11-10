from behave.fixture import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context) -> webdriver.Chrome:
    context.browser = webdriver.Chrome()
    context.browser.set_window_size(1920, 1080)
    yield context.browser
    context.browser.quit()


#def before_all(context):
#    use_fixture(selenium_browser_chrome, context)