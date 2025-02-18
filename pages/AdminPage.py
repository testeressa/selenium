from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageAdmin:

    USERNAME = 'user'
    PASSWORD = 'bitnami'
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type = 'submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def input_username(self):
        self.browser.find_element(*self.INPUT_USERNAME).clear()
        self.browser.find_element(*self.INPUT_USERNAME).send_keys(self.USERNAME)

    def input_password(self):
        self.browser.find_element(*self.INPUT_PASSWORD).clear()
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(self.PASSWORD)

    def submit_login(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def logout(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def login_admin_page(self):
        self.input_username()
        self.input_password()
        self.submit_login()



