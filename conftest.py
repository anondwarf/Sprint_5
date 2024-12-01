# coding=utf-8
import pytest
from selenium import webdriver

from src.utils import UtilsForTests


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def random_string(request):
    return UtilsForTests.generate_random_string(request.param)


@pytest.fixture
def random_password(request):
    return UtilsForTests.generate_random_string(request.param)


@pytest.fixture
def random_email(request):
    return UtilsForTests.generate_random_email(request.param)
