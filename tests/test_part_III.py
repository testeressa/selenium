import time

from pages.AdminPage import PageAdmin
from pages.CatalogPage import PageCatalog
from pages.MainPage import PageMain


from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login_succeed_and_logout(browser, ):
    page_admin = PageAdmin(browser)
    page_admin.open(browser.url + "/administration")
    page_admin.login_admin_page()
    WebDriverWait(browser, 2).until(EC.title_contains("Dashboard"))

    assert "Dashboard" in browser.title, "Пользователь не залогинен"
    page_admin.logout()

    WebDriverWait(browser, 2).until(EC.title_contains("Administration"))

    assert "Administration" in browser.title, "Пользователь не разлогинен"


def test_add_item(browser):
    browser.get(browser.url + "/home")
    product = EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-shopping-cart"))
    wait = WebDriverWait(browser, 10)
    ActionChains(browser).move_to_element(wait.until(product)).click().perform()

    browser.get(browser.url + '/en-gb?route=checkout/cart')
    shopping_cart = browser.find_elements(By.CSS_SELECTOR, "#shopping-cart")

    assert len(shopping_cart) == 1, f'Товар не был добавлен в корзину'


def test_currency_change_main_page(browser):
    page_main = PageMain(browser)
    page_main.open(browser.url + "/home")
    initial_currency = page_main.get_current_currency()

    page_main.open_currency_dropdown()
    time.sleep(3)

    page_main.select_currency(0)
    updated_currency = page_main.get_current_currency()

    assert initial_currency != updated_currency[0], f'Изменение валюты не применилось'


def test_currency_change_catalog(browser):
    page_catalog = PageCatalog(browser)
    page_catalog.open(browser.url + "/catalog/desktops")
    initial_currency = page_catalog.get_current_currency()

    page_catalog.open_currency_dropdown()
    time.sleep(1)

    page_catalog.select_currency()
    time.sleep(1)

    updated_currency = page_catalog.get_current_currency()

    assert initial_currency != updated_currency, f'Изменение валюты не применилось'


