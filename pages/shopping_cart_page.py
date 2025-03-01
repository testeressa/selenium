from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class PageShoppingCart(BasePage):
    CART_TABLE = (By.CSS_SELECTOR, "#shopping-cart")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".fa-shopping-cart")

    def get_shopping_cart_items(self):
        self.logger.debug(f"{self.class_name}: Getting shopping cart items 'CART TABLE'")
        return self.browser.find_elements(*self.CART_TABLE)

    def add_item_to_cart(self):
        self.logger.info(f"{self.class_name}: Adding item to cart")
        add_to_cart_button = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON)
        )
        ActionChains(self.browser).move_to_element(add_to_cart_button).click().perform()
