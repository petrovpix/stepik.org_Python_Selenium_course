from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
import time
import math

try:
    op = webdriver.FirefoxOptions()
    ser = Service("C:\\geckodriver\\geckodriver.exe")
    op.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    browser = webdriver.Firefox(service=ser, options=op)

    #execute small JavaScript in browser
    browser.execute_script("alert('Robots at work');")

finally:

    time.sleep(30)

    browser.quit()
