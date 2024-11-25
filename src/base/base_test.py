from abc import ABC

import pytest

from src.pages import LoginPage, MainPage, RegistrationPage


class BaseTest(ABC):
    """Класс конструктор для всех классов `*Test`"""

    login_page: LoginPage
    main_page: MainPage
    registration_page: RegistrationPage

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.registration_page = RegistrationPage(driver)
