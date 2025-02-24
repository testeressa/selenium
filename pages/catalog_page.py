from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageCatalog(BasePage):
    COMPARE_TOTAL_BUTTON = By.CSS_SELECTOR, "#compare-total"
    GRID_BUTTON = By.CSS_SELECTOR, "#button-grid"
    LIST_BUTTON = By.CSS_SELECTOR, "#button-list"
    ITEM = By.CSS_SELECTOR, ".product-thumb"
    ALERT = By.CSS_SELECTOR, ".alert"

    ACTUAL_PRICE = (By.CSS_SELECTOR, ".price-new")

    def get_current_currency(self):
        return [product.find_element(*self.ACTUAL_PRICE).text
                for product in self.browser.find_elements(*self.ITEM)]
