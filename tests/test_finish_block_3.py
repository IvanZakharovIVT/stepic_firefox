import time

from selenium.webdriver.common.by import By

def test_check_add_to_card_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_item = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button_item.is_displayed()
    time.sleep(30)
