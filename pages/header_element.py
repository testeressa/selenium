import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Header(BasePage):
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item")

    @allure.step('Opening current currency')
    def open_currency_dropdown(self):
        self.logger.debug(f"{self.class_name}: Opening currency dropdown")
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CURRENCY_DROPDOWN)).click()

    @allure.step('Selecting currency')
    def select_currency(self, index=0):
        self.logger.info(f"{self.class_name}: Selecting currency")
        currencies = self.browser.find_elements(*self.CURRENCY_OPTIONS)
        if currencies:
            currencies[index].click()
        else:
            raise AssertionError("Список валют пуст")

    @allure.step('Switching currency')
    def switch_currency(self):
        self.logger.info(f"{self.class_name}: Switching currency")
        self.open_currency_dropdown()
        self.select_currency()
