from selenium.webdriver.common.by import By


def test_main_page(browser):
    browser.get(browser.url + "/home")
    browser.find_element(By.ID, "logo")
    browser.find_element(By.NAME, "search")
    browser.find_element(By.CSS_SELECTOR, "#header-cart > div")
    browser.find_element(By.XPATH, "//*[text()='Currency']")
    browser.find_element(By.CSS_SELECTOR, "#header-cart")


def test_catalog_page(browser):
    browser.get(browser.url + "/catalog/desktops")
    browser.find_element(By.CSS_SELECTOR, "#input-username")
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.CSS_SELECTOR, ".card-header")
    browser.find_element(By.CSS_SELECTOR, ".input-group-text")


def test_item_page(browser):
    browser.get(browser.url + "/product/desktops/apple-cinema")
    browser.find_element(By.CSS_SELECTOR, "#button-cart")
    browser.find_element(By.CSS_SELECTOR, ".price-old")
    browser.find_element(By.CSS_SELECTOR, "#input-option-value-5")
    browser.find_element(By.CSS_SELECTOR, ".form-select")
    link = browser.find_element(
        By.XPATH, "//a[contains(@href,'apple?route=product/manufacturer.info')]")
    link.click()


def test_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.CSS_SELECTOR, "#input-username")
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.CSS_SELECTOR, ".card-header")
    browser.find_element(By.CSS_SELECTOR, ".input-group-text")


def test_registration_page(browser):
    browser.get(browser.url + "/en-gb?route=account/register")
    browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.CSS_SELECTOR, ".modal-link")
