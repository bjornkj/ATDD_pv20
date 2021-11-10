import time

from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()


browser.get("https://lambdatest.github.io/sample-todo-app/")
# "//ul/li"

time.sleep(3)
for element in browser.find_elements(By.XPATH, "//ul/li"):
    print(element.text)
    element.find_element(By.XPATH, "input").click()
    element.click()

time.sleep(15)