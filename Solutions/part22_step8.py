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
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # filled all * input
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("ivan@bolvan.com")
    element = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # get path in OS to this .py file
    file_path = os.path.join(current_dir, 'new.txt')  # main path (.py file path) + new.txt
    element.send_keys(file_path) #send file in form

    # submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(1)

finally:

    time.sleep(30)

    browser.quit()
