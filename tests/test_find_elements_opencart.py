import allure

from selenium.webdriver.common.by import By
from pages.main_page import PageMain
from pages.product_page import PageProduct
from pages.catalog_page import PageCatalog
from pages.admin_page import PageAdmin
from pages.registration_page import PageRegistration
from pages.header_element import Header


@allure.title("Проврека наличия элементов на главной странице")
def test_main_page(browser):
    browser.get(browser.url + "/home")
    browser.find_element(*PageMain.LOGO_BUTTON)
    browser.find_element(*PageMain.SEARCH)
    browser.find_element(By.CSS_SELECTOR, "#header-cart > div")
    browser.find_element(*Header.CURRENCY_DROPDOWN)
    browser.find_element(By.CSS_SELECTOR, "#header-cart")


@allure.title("Проврека наличия элементов на странице каталога")
def test_catalog_page(browser):
    browser.get(browser.url + "/catalog/desktops")
    browser.find_element(*PageCatalog.COMPARE_TOTAL_BUTTON)
    browser.find_element(*PageCatalog.LIST_BUTTON)
    browser.find_element(*PageCatalog.GRID_BUTTON)
    browser.find_element(*PageCatalog.ITEM)
    browser.find_element(By.XPATH, "//a[contains(@href,'catalog/desktops/mac')]")


@allure.title("Проврека наличия элементов на странице товара")
def test_product_page(browser):
    browser.get(browser.url + "/product/desktops/apple-cinema")
    browser.find_element(*PageProduct.ADD_TO_CARD_BUTTON)
    browser.find_element(*PageProduct.OLD_PRICE)
    browser.find_element(By.CSS_SELECTOR, "#input-option-value-5")
    browser.find_element(*PageProduct.SELECT_COLOR)
    browser.find_element(By.XPATH, "//a[contains(@href,'apple?route=product/manufacturer.info')]")

@allure.title("Проврека наличия элементов на странице логина")
def test_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*PageAdmin.INPUT_USERNAME)
    browser.find_element(*PageAdmin.INPUT_PASSWORD)
    browser.find_element(*PageAdmin.SUBMIT_BUTTON)
    browser.find_element(By.CSS_SELECTOR, ".card-header")
    browser.find_element(By.CSS_SELECTOR, ".input-group-text")


@allure.title("Проврека наличия элементов на странице регистрации")
def test_registration_page(browser):
    browser.get(browser.url + "/en-gb?route=account/register")
    browser.find_element(*PageRegistration.FIRSTNAME)
    browser.find_element(*PageRegistration.PASSWORD)
    browser.find_element(*PageRegistration.SUBSCRIBE_TOGGLE)
    browser.find_element(*PageRegistration.CONTINUE_BUTTON)
    browser.find_element(By.CSS_SELECTOR, ".modal-link")
