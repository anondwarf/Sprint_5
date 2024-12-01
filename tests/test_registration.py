# coding=utf-8
import pytest
from selenium.webdriver.common.by import By

from src.locators import Locators


class TestRegistration:
    REGISTRATION_URL: str = "https://stellarburgers.nomoreparties.site/register"
    LOGIN_URL: str = "https://stellarburgers.nomoreparties.site/login"

    @pytest.mark.parametrize(
        "random_string, random_email, random_password", [(5, 10, 7)]
    )
    def test_registration_good_param(
        self, driver, random_string, random_email, random_password
    ):

        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_NAME_INPUT).send_keys(
            random_string
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_EMAIL_INPUT).send_keys(
            random_email
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            random_password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        assert driver.current_url == TestRegistration.REGISTRATION_URL

    @pytest.mark.parametrize("random_password", [4])
    def test_registration_bad_param(self, driver, random_password):
        driver.get(TestRegistration.REGISTRATION_URL)
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys(
            random_password
        )
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTTON).click()
        element = driver.find_element(By.XPATH, Locators.REGISTRATION_ERROR_PASSWORD)
        assert element is not None
