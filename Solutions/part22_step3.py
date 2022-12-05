from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
import time
import math

# options conf for Firefox and WebDriver
ser = Service("C:\\geckodriver\\geckodriver.exe")
op = webdriver.FirefoxOptions()
op.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
browser = webdriver.Firefox(service=ser, options=op)

link = "https://suninjuly.github.io/selects2.html"
browser.get(link)

a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
a = a_element.text

b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
b = b_element.text

add_a_b = int(a) + int(b)

answr_element = browser.find_element(By.CSS_SELECTOR, "#dropdown")
select = Select(answr_element)
select.select_by_visible_text(str(add_a_b))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)



