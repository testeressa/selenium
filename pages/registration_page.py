import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PageRegistration(BasePage):
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REGISTER_LINK = (By.CSS_SELECTOR, ".fa-user")
    REGISTER_BUTTON = (By.LINK_TEXT, "Register")
    SUBSCRIBE_TOGGLE = (By.CSS_SELECTOR, "#input-newsletter")
    AGREEMENT_TOGGLE = (By.CSS_SELECTOR, "input[name='agree']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")

    def navigate_to_register(self):
        self.logger.info(f"{self.class_name}: Going to register page")
        self.browser.find_element(*self.REGISTER_LINK).click()
        self.browser.find_element(*self.REGISTER_BUTTON).click()

    def register_user(self, first_name, last_name, email, password):
        self.logger.info(f"{self.class_name}: Registering user")
        self.browser.find_element(*self.FIRSTNAME).send_keys(first_name)
        self.browser.find_element(*self.LASTNAME).send_keys(last_name)
        self.browser.find_element(*self.EMAIL).send_keys(email)
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        WebDriverWait(self.browser, 4).until(EC.element_to_be_clickable(self.AGREEMENT_TOGGLE)).click()
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    @allure.step('Checking success of user registration')
    def is_registration_successful(self):
        self.logger.info(f"{self.class_name}: Checking success of user registration")
        return self.browser.title == "Your Account Has Been Created!"

