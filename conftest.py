import pytest
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_config():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    browser.config.driver_options = options
