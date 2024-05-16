from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser,20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button2.click()
finally:
    browser.quit()