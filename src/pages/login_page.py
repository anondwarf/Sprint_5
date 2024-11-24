from src.base import BasePage
from src.config import Links


class LoginPage(BasePage):
    """Страница авторизации"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.LOGIN_URL
