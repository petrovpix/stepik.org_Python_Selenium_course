from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    chkbx = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chkbx.click()

    rdbx = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rdbx.click()

    # submit filled form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    
    time.sleep(30)
    
    browser.quit()
