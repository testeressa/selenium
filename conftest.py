import os
import logging
import allure
import datetime
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
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    url = request.config.getoption("url")
    log_level = request.config.getoption("--log_level")

    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{logs_dir}/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test started at %s" % datetime.datetime.now())

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

    driver.get(url)
    driver.url = url

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    def end():
        driver.quit()
        logger.info("===> Test finished at %s" % datetime.datetime.now())

    request.addfinalizer(end)

    yield driver

    if request.node.rep_call.failed:
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )
