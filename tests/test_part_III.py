import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login_succeed_and_logout(login, browser):
    assert "Dashboard" in login.title, "Пользователь не залогинен"
    logout_button = browser.find_element(By.CSS_SELECTOR, "#nav-logout")
    logout_button.click()


def test_add_item(browser):
    browser.get(browser.url + "/home")
    product = EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-shopping-cart"))
    wait = WebDriverWait(browser, 10)
    ActionChains(browser).move_to_element(wait.until(product)).click().perform()

    browser.get(browser.url + '/en-gb?route=checkout/cart')
    shopping_cart = browser.find_elements(By.CSS_SELECTOR, "#shopping-cart")

    assert len(shopping_cart) == 1, f'Товар не был добавлен в корзину'


def test_currency_change_main_page(browser, get_current_currency):
    browser.get(browser.url + "/home")
    initial_currency = get_current_currency
    currency_dropdown = browser.find_element(By.CSS_SELECTOR, "#form-currency")
    currency_dropdown.click()

    time.sleep(1)

    currencies = browser.find_elements(By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item")
    if currencies:
        currencies[0].click()
    else:
        raise AssertionError("Список валют пуст")

    time.sleep(1)

    updated_currency = [product.find_element(By.CSS_SELECTOR, ".price-new").text
                        for product in browser.find_elements(By.CSS_SELECTOR, ".product-thumb")]

    time.sleep(1)

    assert initial_currency != updated_currency[0], f'Изменение валюты не применилось'


def test_currency_change_catalog(browser,get_current_currency):
    browser.get(browser.url + "/catalog/desktops")
    initial_currency = get_current_currency
    currency_dropdown = browser.find_element(By.CSS_SELECTOR, "#form-currency")
    currency_dropdown.click()

    time.sleep(1)

    currencies = browser.find_elements(By.CSS_SELECTOR, ".dropdown-menu.show .dropdown-item")
    if currencies:
        currencies[0].click()
    else:
        raise AssertionError("Список валют пуст")

    time.sleep(1)

    updated_currency = [product.find_element(By.CSS_SELECTOR, ".price-new").text
                        for product in browser.find_elements(By.CSS_SELECTOR, ".product-thumb")]

    assert initial_currency != updated_currency[0], f'Изменение валюты не применилось'


