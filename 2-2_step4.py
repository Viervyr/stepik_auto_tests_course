from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    browser.quit()
