from src.base import BasePage
from src.config import Links


class RegistrationPage(BasePage):
    """Страница регистрации"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.REGISTER_URL
