from src.base import BaseTest
from src.config import AccountProfilePageLocators as Appl
from src.config import BasePageLocators as Bpl
from src.config import LoginPageLocators as Lpl


class TestAccountExit(BaseTest):
    """Тест выхода из профиля"""

    def test_exit_account(self) -> None:
        self.login_page.open()
        self.login_page.enter_text(
            locator=Lpl.LOGIN_INPUT, text_="antonbogomolov12a1234@ya.ru"
        )
        self.login_page.enter_text(locator=Lpl.PASSWORD_INPUT, text_="1234567")
        self.login_page.click(locator=Lpl.LOGIN_BUTTON)
        self.main_page.click(locator=Bpl.ACCOUNT_LINK)
        self.account_profile_page.click(Appl.EXIT_BUTTON)
        self.main_page.click(Bpl.ACCOUNT_LINK)
        self.login_page.is_opened()
