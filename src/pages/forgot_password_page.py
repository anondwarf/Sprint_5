from src.base import BasePage
from src.config import Links


class ForgotPasswordPage(BasePage):
    """Станица восстановления пароля"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.FORGOT_PASSWORD_URL
