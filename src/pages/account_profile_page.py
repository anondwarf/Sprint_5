from src.base import BasePage
from src.config import Links


class AccountProfilePage(BasePage):
    """Страница профиля"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = Links.ACCOUNT_PROFILE_PAGE
