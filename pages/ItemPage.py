from selenium.webdriver.common.by import By


class PageItem:
    ADD_TO_CARD_BUTTON = By.CSS_SELECTOR, "#button-cart"
    OLD_PRICE = By.CSS_SELECTOR, ".price-old"
    SELECT_COLOR = By.CSS_SELECTOR, ".form-select"

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

