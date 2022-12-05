from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # filed all * input
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("ivan@bolvan.com")

    # submit form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # check registration 
    # wait page load
    time.sleep(1)

    # find element with text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # save in welcome_text from welcome_text_elt
    welcome_text = welcome_text_elt.text

    # assert help to compare real text on page with expected text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # wait for 10sec to check result of script
    time.sleep(10)
    # browser close
    browser.quit()
