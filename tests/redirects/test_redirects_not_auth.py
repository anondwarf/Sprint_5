from src.base import BaseTest
from src.config import BasePageLocators as Bpl
from src.config import ForgotPasswordPageLocators as Fppl
from src.config import MainPageLocators as Mpl
from src.config import RegistrationPageLocators as Rpl


class TestRedirectNotAuth(BaseTest):
    """Тестирование редиректов на проекте"""

    def test_main_page_login_account_button(self):
        self.main_page.open()
        self.main_page.click(locator=Mpl.LOGIN_ACCOUNT_BUTTON)
        self.login_page.is_opened()

    def test_base_page_account_link(self):
        self.main_page.open()
        self.main_page.click(locator=Bpl.ACCOUNT_LINK)
        self.login_page.is_opened()

    def test_registration_page_login_link(self):
        self.registration_page.open()
        self.registration_page.click(locator=Rpl.LOGIN_LINK)
        self.login_page.is_opened()

    def test_forgot_password_login_link(self):
        self.forgot_password_page.open()
        self.forgot_password_page.click(locator=Fppl.LOGIN_LINK)
        self.login_page.is_opened()
