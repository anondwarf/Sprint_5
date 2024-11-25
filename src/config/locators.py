class BasePageLocators:
    """Локаторы BasePage"""


class MainPageLocators:
    """Локаторы MainPage"""


class LoginPageLocators:
    """Локаторы LoginPage"""


class RegistrationPageLocators:
    """Локаторы RegistrationPage"""

    NAME_INPUT: tuple[str, str] = (
        "xpath",
        "//label[contains(text(), 'Имя')]/following::input[1]",
    )
    EMAIL_INPUT: tuple[str, str] = (
        "xpath",
        "//label[contains(text(), 'Email')]/following::input[1]",
    )
    PASSWORD_INPUT: tuple[str, str] = (
        "xpath",
        "//label[contains(text(), 'Пароль')]/following::input[1]",
    )
    REGISTRATION_BUTTON: tuple[str, str] = (
        "xpath",
        "//button[contains(text(), 'Зарегистрироваться')]",
    )
    LOGIN_LINK: tuple[str, str] = ("xpath", "//a[@href='/login']")
    PASSWORD_ERROR_NOTICE: tuple[str, str] = (
        "xpath",
        "//p[contains(text(), 'Некорректный')]",
    )
    PASSWORD_ERROR_INPUT: tuple[str, str] = (
        "xpath",
        "//div[contains(@class, 'error')]",
    )
    USER_ERROR_NOTICE: tuple[str, str] = (
        "xpath",
        "//p[contains(@class, 'error')]",
    )
