from selenium.webdriver.common.by import By

from pages.MainPage import PageMain
from pages.ItemPage import PageItem
from pages.CatalogPage import PageCatalog
from pages.AdminPage import PageAdmin
from pages.RegistrationPage import PageRegistration


def test_main_page(browser):
    browser.get(browser.url + "/home")
    browser.find_element(*PageMain.LOGO_BUTTON)
    browser.find_element(*PageMain.SEARCH)
    browser.find_element(By.CSS_SELECTOR, "#header-cart > div")
    browser.find_element(*PageMain.CURRENCY_DROPDOWN)
    browser.find_element(By.CSS_SELECTOR, "#header-cart")


def test_catalog_page(browser):
    browser.get(browser.url + "/catalog/desktops")
    browser.find_element(*PageCatalog.COMPARE_TOTAL_BUTTON)
    browser.find_element(*PageCatalog.LIST_BUTTON)
    browser.find_element(*PageCatalog.GRID_BUTTON)
    browser.find_element(*PageCatalog.ITEM)
    browser.find_element(By.XPATH, "//a[contains(@href,'catalog/desktops/mac')]")


def test_item_page(browser):
    browser.get(browser.url + "/product/desktops/apple-cinema")
    browser.find_element(*PageItem.ADD_TO_CARD_BUTTON)
    browser.find_element(*PageItem.OLD_PRICE)
    browser.find_element(By.CSS_SELECTOR, "#input-option-value-5")
    browser.find_element(*PageItem.SELECT_COLOR)
    browser.find_element(By.XPATH, "//a[contains(@href,'apple?route=product/manufacturer.info')]").click()


def test_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*PageAdmin.INPUT_USERNAME)
    browser.find_element(*PageAdmin.INPUT_PASSWORD)
    browser.find_element(*PageAdmin.SUBMIT_BUTTON)
    browser.find_element(By.CSS_SELECTOR, ".card-header")
    browser.find_element(By.CSS_SELECTOR, ".input-group-text")


def test_registration_page(browser):
    browser.get(browser.url + "/en-gb?route=account/register")
    browser.find_element(*PageRegistration.FIRSTNAME)
    browser.find_element(*PageRegistration.INPUT_PASSWORD)
    browser.find_element(*PageRegistration.SUBSCRIBE_TOGGLE)
    browser.find_element(*PageRegistration.CONTINUE_BUTTON)
    browser.find_element(By.CSS_SELECTOR, ".modal-link")
