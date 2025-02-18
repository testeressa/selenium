from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCatalog:
    COMPARE_TOTAL_BUTTON = By.CSS_SELECTOR, "#compare-total"
    GRID_BUTTON = By.CSS_SELECTOR, "#button-grid"
    LIST_BUTTON = By.CSS_SELECTOR, "#button-list"
    ITEM = By.CSS_SELECTOR, ".product-thumb"
    ALERT = By.CSS_SELECTOR, ".alert"

    ACTUAL_PRICE = (By.CSS_SELECTOR, ".price-new")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item")

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def get_current_currency(self):
        return [product.find_element(*self.ACTUAL_PRICE).text
                for product in self.browser.find_elements(*self.ITEM)]

    def open_currency_dropdown(self):
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CURRENCY_DROPDOWN)).click()

    def select_currency(self, index=0):
        currencies = self.browser.find_elements(*self.CURRENCY_OPTIONS)
        if currencies:
            currencies[index].click()
        else:
            raise AssertionError("Список валют пуст")
