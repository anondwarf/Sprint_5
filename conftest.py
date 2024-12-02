# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.utils import UtilsForTests


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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
