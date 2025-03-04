import allure

from pages.admin_page import PageAdmin
from pages.catalog_page import PageCatalog
from pages.main_page import PageMain
from pages.header_element import Header
from pages.registration_page import PageRegistration
from pages.shopping_cart_page import PageShoppingCart


@allure.title("Проврека логина, разлогина в админке")
def test_login_succeed_and_logout(browser, ):
    page_admin = PageAdmin(browser)
    page_admin.open(browser.url + "/administration")
    page_admin.login_admin_page()
    page_admin.wait_for_title()

    assert "Dashboard" in browser.title, "Редирект на страницу дашборда не выполнен"
    assert page_admin.logout_button_is_displayed(), "Кнопка логаута на странице не обнаружена"
    assert page_admin.name_is_displayed(), "Имя пользователя не выводится"

    page_admin.logout()
    page_admin.wait_for_title(title_text="Administration")

    assert "Administration" in browser.title, "Пользователь не разлогинен"


@allure.title("Проврека добавления товара в корзину")
def test_add_item(browser):
    page_shopping_cart = PageShoppingCart(browser)
    page_shopping_cart.open(browser.url + "/home")

    page_shopping_cart.add_item_to_cart()

    page_shopping_cart.open(browser.url + '/en-gb?route=checkout/cart')
    shopping_cart = page_shopping_cart.get_shopping_cart_items()

    assert len(shopping_cart) == 1, 'Товар не был добавлен в корзину'


@allure.title("Проврека изменения валюты на главной странице")
def test_currency_change_main_page(browser):
    page_main = PageMain(browser)
    page_main.open(browser.url + "/home")
    initial_currency = page_main.get_current_currency()

    header = Header(browser)
    header.open_currency_dropdown()
    header.select_currency(0)
    updated_currency = page_main.get_current_currency()

    assert initial_currency != updated_currency, 'Изменение валюты не применилось'


@allure.title("Проврека изменения валюты в каталоге")
def test_currency_change_catalog(browser):
    page_catalog = PageCatalog(browser)
    page_catalog.open(browser.url + "/catalog/desktops")
    initial_currency = page_catalog.get_current_currency()

    header = Header(browser)
    header.open_currency_dropdown()
    header.select_currency()
    updated_currency = page_catalog.get_current_currency()

    assert initial_currency != updated_currency, 'Изменение валюты не применилось'


@allure.title("Проврека добавления товара в админке")
def test_add_new_product(browser):
    page_admin = PageAdmin(browser)
    page_admin.open(browser.url + "/administration")
    page_admin.login_admin_page()
    page_admin.navigate_to_products()
    initial_products_count = page_admin.get_products_count()
    page_admin.add_new_product(
        "Test Product", "Test Meta Tag", "Test Model", "test-keyword00---002"
    )

    assert page_admin.is_success_message_displayed(), "Сообщение о добавлении товара отображено на странице"

    page_admin.navigate_to_products()
    updated_products_count = page_admin.get_products_count()

    assert initial_products_count < updated_products_count, "Товар не был добавлен"


@allure.title("Проврека удаления товара в админке")
def test_delete_product(browser):
    page_admin = PageAdmin(browser)
    page_admin.open(browser.url + "/administration")
    page_admin.login_admin_page()
    page_admin.navigate_to_products()
    page_admin.delete_product()
    assert page_admin.is_success_message_displayed(), "Товар не был удален"


@allure.title("Проврека регистрации нового пользователя")
def test_register_new_user(browser):
    page_reg = PageRegistration(browser)
    page_reg.open(browser.url)
    page_reg.navigate_to_register()
    page_reg.register_user("Test1", "User1", "test1.user1@example.com", "password1")
    assert page_reg.is_registration_successful(), "Регистрация не удалась"


@allure.title("Проврека переключения между валютами")
def test_switch_currency(browser):
    header = Header(browser)
    header.open(browser.url)
    header.switch_currency()
    page_main = PageMain(browser)
    assert "€" in page_main.get_current_currency()[-1], "Валюта не была изменена"
