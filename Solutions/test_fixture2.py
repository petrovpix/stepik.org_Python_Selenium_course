import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# Mozilla RUN options
op = webdriver.FirefoxOptions()
ser = Service("C:\\geckodriver\\geckodriver.exe")
op.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox(service=ser, options=op)
    browser.implicitly_wait(10)
    return browser


class TestMainPage1():
    # call fixture browser, it set as argument
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")