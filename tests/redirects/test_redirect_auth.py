from src.base import BaseTest
from src.config import BasePageLocators as Bpl
from src.config import LoginPageLocators as Lpl


class TestRedirectAuth(BaseTest):
    """Тесты редиректов, когда пользователь авторизован"""

    def test_main_page_login_link(self) -> None:
        self.login_page.open()
        self.login_page.enter_text(
            locator=Lpl.LOGIN_INPUT, text_="antonbogomolov12a1234@ya.ru"
        )
        self.login_page.enter_text(locator=Lpl.PASSWORD_INPUT, text_="1234567")
        self.login_page.click(locator=Lpl.LOGIN_BUTTON)
        self.main_page.open()
        self.main_page.click(locator=Bpl.ACCOUNT_LINK)
        self.account_profile_page.is_opened()

    def test_account_profile_page_constructor_link(self) -> None:
        self.login_page.open()
        self.login_page.enter_text(
            locator=Lpl.LOGIN_INPUT, text_="antonbogomolov12a1234@ya.ru"
        )
        self.login_page.enter_text(locator=Lpl.PASSWORD_INPUT, text_="1234567")
        self.login_page.click(locator=Lpl.LOGIN_BUTTON)
        self.main_page.click(Bpl.ACCOUNT_LINK)
        self.account_profile_page.click(locator=Bpl.CONSTRUCTOR_LINK)
        self.main_page.is_opened()

    def test_account_profile_page_logo(self) -> None:
        self.login_page.open()
        self.login_page.enter_text(
            locator=Lpl.LOGIN_INPUT, text_="antonbogomolov12a1234@ya.ru"
        )
        self.login_page.enter_text(locator=Lpl.PASSWORD_INPUT, text_="1234567")
        self.login_page.click(locator=Lpl.LOGIN_BUTTON)
        self.account_profile_page.open()
        self.account_profile_page.click(Bpl.LOGO_LINK)
        self.main_page.is_opened()
