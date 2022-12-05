from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
import time
import math


op = webdriver.FirefoxOptions()
ser = Service("C:\\geckodriver\\geckodriver.exe")
op.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
browser = webdriver.Firefox(service=ser, options=op)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #scroll with JavaScript

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    chkbx = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chkbx.click()

    rdbx = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rdbx.click()

    button.click()

    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
