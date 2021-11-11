from behave.fixture import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context) -> webdriver.Chrome:
    context.browser = webdriver.Chrome()
    context.browser.set_window_size(1920, 1080)
    yield context.browser
    context.browser.quit()


# def before_all(context):
#     use_fixture(selenium_browser_chrome, context)


def before_scenario(context, scenario):
    if "web" in scenario.tags:
        use_fixture(selenium_browser_chrome, context)




# Hooks, vi definierar funktioner, verktyget kör dom vid rätt tillfälle om dom finns
# before_feature(context, feature) körs innan varje feature
# before_scenario(context, scenario)
# before_step(context, step)
# before_tag(context, tag)
# before_all(context) # körs först

# after_all(context)
# after_tag(context, tag)
# after_step(context, step)
# after_scenario(context, scenario)
# after_feature(context, feature)

