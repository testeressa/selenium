from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.catalog_page import PageCatalog


class PageMain(BasePage):
    LOGO_BUTTON = (By.ID, "logo")
    SEARCH = (By.NAME, "search")
    CURRENCY_BUTTON = (By.XPATH, "//*[text()='Currency']")
    ACTUAL_PRICE = (By.CSS_SELECTOR, ".price-new")

    def get_current_currency(self):
        self.logger.info(f"{self.class_name}: Getting current currency")
        return [product.find_element(*self.ACTUAL_PRICE).text
                for product in self.browser.find_elements(*PageCatalog.ITEM)]
