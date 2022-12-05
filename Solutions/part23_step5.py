from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
import time
import math
import os

op = webdriver.FirefoxOptions()
ser = Service("C:\\geckodriver\\geckodriver.exe")
op.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
browser = webdriver.Firefox(service=ser, options=op)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, ".trollface.btn-primary")
    button1.click()

    time.sleep(1)

    print(browser.window_handles)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) #switch between windows/tabs in browser

    time.sleep(2)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button2.click()

    time.sleep(1)

finally:
    time.sleep(30)

    browser.quit()
