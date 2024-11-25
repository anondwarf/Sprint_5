import pytest
from selenium import webdriver

from src.config import BrowsersOptions
from src.utils import GenerationData


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(options=BrowsersOptions.chrome_options())
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def generate_string(request):
    return GenerationData.generate_string(request.param)


@pytest.fixture
def generate_email(request):
    return GenerationData.generate_email(request.param)
