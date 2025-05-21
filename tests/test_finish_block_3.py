from selenium.webdriver.common.by import By

def test_finish_block_3(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_list = [element.text for element in browser.find_elements(By.XPATH, "//button[@type='submit']")]
    assert "Добавить в корзину" in button_list
