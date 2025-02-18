from pages.admin_page import PageAdmin
from pages.catalog_page import PageCatalog
from pages.main_page import PageMain
from pages.header_element import Header
from pages.shopping_cart_page import PageShoppingCart


def test_login_succeed_and_logout(browser, ):
    page_admin = PageAdmin(browser)
    page_admin.open(browser.url + "/administration")
    page_admin.login_admin_page()

    page_admin.wait_for_title()

    assert "Dashboard" in browser.title, "Пользователь не залогинен"

    page_admin.logout()
    page_admin.wait_for_title(title_text="Administration")

    assert "Administration" in browser.title, "Пользователь не разлогинен"


def test_add_item(browser):
    page_shopping_cart = PageShoppingCart(browser)
    page_shopping_cart.open(browser.url + "/home")

    page_shopping_cart.add_item_to_cart()

    page_shopping_cart.open(browser.url + '/en-gb?route=checkout/cart')
    shopping_cart = page_shopping_cart.get_shopping_cart_items()

    assert len(shopping_cart) == 1, f'Товар не был добавлен в корзину'


def test_currency_change_main_page(browser):
    page_main = PageMain(browser)
    page_main.open(browser.url + "/home")
    initial_currency = page_main.get_current_currency()

    header = Header(browser)
    header.open_currency_dropdown()
    header.select_currency(0)
    updated_currency = page_main.get_current_currency()

    assert initial_currency != updated_currency, f'Изменение валюты не применилось'


def test_currency_change_catalog(browser):
    page_catalog = PageCatalog(browser)
    page_catalog.open(browser.url + "/catalog/desktops")
    initial_currency = page_catalog.get_current_currency()

    header = Header(browser)
    header.open_currency_dropdown()
    header.select_currency()
    updated_currency = page_catalog.get_current_currency()

    assert initial_currency != updated_currency, f'Изменение валюты не применилось'


