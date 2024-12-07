# coding=utf-8
from selenium.webdriver.common.by import By

from src.locators import Locators


class TestRedirects:

    MAIN_PAGE: str = "https://stellarburgers.nomoreparties.site"
    LOGIN_PAGE: str = f"{MAIN_PAGE}/login"
    REGISTER_PAGE: str = f"{MAIN_PAGE}/register"
    FORGOT_PASSWORD_PAGE: str = f"{MAIN_PAGE}/forgot-password"

    def test_main_to_login(self, driver):
        driver.get(TestRedirects.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.MAIN_ENTER_ACCOUNT_BUTTON).click()
        url = driver.current_url
        assert url == TestRedirects.LOGIN_PAGE

    def test_header_to_login(self, driver):
        driver.get(TestRedirects.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.HEADER_ENTER_LINK).click()
        url = driver.current_url
        assert url == TestRedirects.LOGIN_PAGE

    def test_register_to_login(self, driver):
        driver.get(TestRedirects.REGISTER_PAGE)
        driver.find_element(By.XPATH, Locators.REGISTRATION_ENTER_LINK).click()
        url = driver.current_url
        assert url == TestRedirects.LOGIN_PAGE

    def test_forgot_password_to_login(self, driver):
        driver.get(TestRedirects.FORGOT_PASSWORD_PAGE)
        driver.find_element(By.XPATH, Locators.FORGOT_PASS_ENTER_LINK).click()
        url = driver.current_url
        assert url == TestRedirects.LOGIN_PAGE
