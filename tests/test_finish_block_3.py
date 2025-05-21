from selenium.webdriver.common.by import By

def test_finish_block_3(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_item = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button_item.is_displayed()
