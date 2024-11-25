from src.base import BaseTest
from src.config import MainPageLocators as Mpl


class TestConstructor(BaseTest):
    """Тестирование конструктора на главной странице"""

    def test_click_fillings_tab(self):
        self.main_page.open()
        self.main_page.click(Mpl.TOPPINGS_TAB)
        self.main_page.is_displayed(Mpl.TOPPINGS_TITLE)

    def test_click_sauces_tab(self):
        self.main_page.open()
        self.main_page.click(Mpl.SAUCES_TAB)
        self.main_page.is_displayed(Mpl.SAUCES_TITLE)

    def test_click_bread_tab(self):
        self.main_page.open()
        self.main_page.click(Mpl.TOPPINGS_TAB)
        self.main_page.click(Mpl.BREAD_TAB)
        self.main_page.is_displayed(Mpl.BREAD_TITLE)
