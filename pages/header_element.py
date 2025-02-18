from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header:
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item")

    def __init__(self, browser):
        self.browser = browser

    def open_currency_dropdown(self):
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CURRENCY_DROPDOWN)).click()

    def select_currency(self, index=0):
        currencies = self.browser.find_elements(*self.CURRENCY_OPTIONS)
        if currencies:
            currencies[index].click()
        else:
            raise AssertionError("Список валют пуст")
