import pytest

from src.base import BaseTest
from src.config import RegistrationPageLocators as Rpl


class TestRegistration(BaseTest):
    """Тесты страницы регистрации и процесса регистрации"""

    @pytest.mark.parametrize(
        "generate_string",
        [5],
        indirect=True,
        ids=["Name length 5"],
    )
    def test_name_input(self, generate_string):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.NAME_INPUT, text_=generate_string
        )
        self.registration_page.is_entered_text(
            type_="value", locator=Rpl.NAME_INPUT, text_=generate_string
        )

    @pytest.mark.parametrize(
        "generate_email", [5], indirect=True, ids=["Email length 5"]
    )
    def test_email_input(self, generate_email):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.EMAIL_INPUT, text_=generate_email
        )
        self.registration_page.is_entered_text(
            type_="value", locator=Rpl.EMAIL_INPUT, text_=generate_email
        )

    @pytest.mark.parametrize(
        "generate_string", [8], indirect=True, ids=["Pass length 8"]
    )
    def test_password_input_good(self, generate_string):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.PASSWORD_INPUT, text_=generate_string
        )
        self.registration_page.is_entered_text(
            type_="value", locator=Rpl.PASSWORD_INPUT, text_=generate_string
        )

    @pytest.mark.parametrize(
        "generate_string", [2], indirect=True, ids=["Password length 2"]
    )
    def test_password_input_bad_notice(self, generate_string):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.PASSWORD_INPUT, text_=generate_string
        )
        self.registration_page.is_displayed(locator=Rpl.PASSWORD_ERROR_NOTICE)

    @pytest.mark.parametrize(
        "generate_string", [4], indirect=True, ids=["Password length 4"]
    )
    def test_password_input_bad_input(self, generate_string):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.PASSWORD_INPUT, text_=generate_string
        )
        self.registration_page.is_displayed(locator=Rpl.PASSWORD_ERROR_INPUT)

    @pytest.mark.parametrize(
        "generate_string, generate_email",
        [(7, 7)],
        indirect=True,
        ids=["Length 7"],
    )
    def test_registration(self, generate_string, generate_email):
        self.registration_page.open()
        self.registration_page.enter_text(
            locator=Rpl.NAME_INPUT, text_=generate_string
        )
        self.registration_page.enter_text(
            locator=Rpl.EMAIL_INPUT, text_=generate_email
        )
        self.registration_page.enter_text(
            locator=Rpl.PASSWORD_INPUT, text_=generate_string
        )
        self.registration_page.click(locator=Rpl.REGISTRATION_BUTTON)
        self.login_page.is_opened()
