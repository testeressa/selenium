from selenium.webdriver.common.by import By


class PageRegistration:
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    SUBSCRIBE_TOGGLE = (By.CSS_SELECTOR, "input[type='checkbox']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

