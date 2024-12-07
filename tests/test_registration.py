# coding=utf-8
import time

import pytest
from selenium.webdriver.common.by import By

from src.locators import Locators


class TestRegistration:
    REGISTRATION_URL: str = "https://stellarburgers.nomoreparties.site/register"
    LOGIN_URL: str = "https://stellarburgers.nomoreparties.site/login"
    ACCOUNT_PROFILE_PAGE: str = (
        "https://stellarburgers.nomoreparties.site/account/profile"
    )

    @pytest.mark.parametrize(
        "random_string, random_email, random_password", [(5, 10, 7)], indirect=True
    )
    def test_registration_good_param(
        self, driver, random_string, random_email, random_password
    ):
        email: str = random_email
        password: str = random_password
        login: str = random_string

        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_NAME_INPUT).send_keys(login)
        driver.find_element(By.XPATH, Locators.REGISTRATION_EMAIL_INPUT).send_keys(
            email
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        driver.get(TestRegistration.LOGIN_URL)
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, Locators.LOGIN_ENTER_BUTTON).click()
        driver.get(TestRegistration.ACCOUNT_PROFILE_PAGE)
        assert driver.current_url == TestRegistration.ACCOUNT_PROFILE_PAGE

    @pytest.mark.parametrize("random_password", [4])
    def test_registration_bad_param(self, driver, random_password):
        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            random_password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        element = driver.find_element(By.XPATH, Locators.REGISTRATION_ERROR_PASSWORD)
        assert element is not None
