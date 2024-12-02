# coding=utf-8
import time

from selenium.webdriver.common.by import By

from src.locators import Locators


class TestAccountProfile:
    MAIN_PAGE: str = "https://stellarburgers.nomoreparties.site"
    ACCOUNT_PROFILE_PAGE: str = f"{MAIN_PAGE}/account/profile"
    LOGIN_PAGE: str = f"{MAIN_PAGE}/login"

    def test_redirect_main_to_account_profile(self, driver):
        driver.get(TestAccountProfile.LOGIN_PAGE)
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(
            "antonbogomolov12a1234@ya.ru"
        )
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(
            "1234567"
        )
        driver.find_element(By.XPATH, Locators.LOGIN_ENTER_BUTTON).click()
        time.sleep(2)
        driver.get(TestAccountProfile.MAIN_PAGE)
        driver.find_element(By.XPATH, Locators.HEADER_ENTER_LINK).click()
        url = driver.current_url
        assert url == TestAccountProfile.ACCOUNT_PROFILE_PAGE

    def test_exit_account_profile(self, driver):
        driver.get(TestAccountProfile.LOGIN_PAGE)
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(
            "antonbogomolov12a1234@ya.ru"
        )
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(
            "1234567"
        )
        driver.find_element(By.XPATH, Locators.LOGIN_ENTER_BUTTON).click()
        driver.find_element(By.XPATH, Locators.HEADER_ENTER_LINK).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.ACCOUNT_PROFILE_EXIT_BUTTON).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Locators.HEADER_ENTER_LINK).click()
        url = driver.current_url
        assert url == TestAccountProfile.LOGIN_PAGE
