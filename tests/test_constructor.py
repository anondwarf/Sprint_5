# coding=utf-8
from selenium.webdriver.common.by import By

from src.locators import Locators


class TestConstructor:

    MAIN_PAGE: str = "https://stellarburgers.nomoreparties.site"

    def test_constructor_topping_tab(self, driver):
        driver.get(TestConstructor.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.MAIN_TOPPING_TAB).click()
        element = driver.find_element(By.XPATH, Locators.MAIN_TOPPING_HEADER)
        assert element.is_displayed()

    def test_constructor_sauces_tab(self, driver):
        driver.get(TestConstructor.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.MAIN_SAUCES_TAB).click()
        element = driver.find_element(By.XPATH, Locators.MAIN_TOPPING_HEADER)
        assert element.is_displayed()

    def test_constructor_bread_tab(self, driver):
        driver.get(TestConstructor.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.MAIN_TOPPING_TAB).click()
        driver.find_element(By.XPATH, Locators.MAIN_BREAD_TAB).click()
        element = driver.find_element(By.XPATH, Locators.MAIN_BREAD_HEADER)
        assert element.is_displayed()
