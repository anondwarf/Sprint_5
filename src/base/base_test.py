from abc import ABC

import pytest

from src.pages import (
    AccountProfilePage,
    ForgotPasswordPage,
    LoginPage,
    MainPage,
    RegistrationPage,
)


class BaseTest(ABC):
    """Класс конструктор для всех классов `*Test`"""

    login_page: LoginPage
    main_page: MainPage
    registration_page: RegistrationPage
    forgot_password_page: ForgotPasswordPage
    account_profile_page: AccountProfilePage

    @pytest.fixture(autouse=True)
    def setup(self, driver, request):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.registration_page = RegistrationPage(driver)
        request.cls.forgot_password_page = ForgotPasswordPage(driver)
        request.cls.account_profile_page = AccountProfilePage(driver)
