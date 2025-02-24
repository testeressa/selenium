import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.safari.options import Options as SFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.0.23:8081")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    url = request.config.getoption("url")

    if browser_name in ["Chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["Firefox", "ff"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["Safari", "sf"]:
        options = SFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Safari(options=options)
    elif browser_name in ["Yandex", "ya"]:
        service = Service(executable_path="/Users/maria.kosheleva/Downloads/drivers/yandexdriver")
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.binary_location = "/Applications/Yandex.app"
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url
    
    return driver
