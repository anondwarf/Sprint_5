# coding=utf-8
import pytest
from selenium.webdriver.common.by import By

from src.locators import Locators


class TestRegistration:
    REGISTRATION_URL: str = "https://stellarburgers.nomoreparties.site/register"
    LOGIN_URL: str = "https://stellarburgers.nomoreparties.site/login"

    @pytest.mark.parametrize(
        "username,email,password", [("pupa", "lupa@pupa.com", "password")]
    )
    def test_registration_good_param(self, driver, username, email, password):

        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_NAME_INPUT).send_keys(
            username
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_EMAIL_INPUT).send_keys(
            email
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        assert driver.current_url == TestRegistration.REGISTRATION_URL

    @pytest.mark.parametrize("password", ["1234"])
    def test_registration_bad_param(self, driver, password):
        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        element = driver.find_element(By.XPATH, Locators.REGISTRATION_ERROR_PASSWORD)
        assert element is not None
