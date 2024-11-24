from abc import ABC

import pytest

from src.pages import LoginPage, MainPage


class BaseTest(ABC):
    """Класс конструктор для всех классов `*Test`"""

    login_page: LoginPage
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
