import pytest
from selenium import webdriver

from src.config import BrowsersOptions


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Firefox(options=BrowsersOptions.firefox_options())
    request.cls.driver = driver
    yield driver
    driver.quit()
