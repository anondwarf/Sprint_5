class BasePageLocators:
    """Локаторы BasePage"""

    ACCOUNT_LINK: tuple[str, str] = ("xpath", "//a[@href='/account']")
    CONSTRUCTOR_LINK: tuple[str, str] = (
        "xpath",
        "//a[@href='/' and contains(@class, 'AppHeader')]",
    )
    LOGO_LINK: tuple[str, str] = ("xpath", "//a[@class='active']")


class MainPageLocators:
    """Локаторы MainPage"""

    LOGIN_ACCOUNT_BUTTON: tuple[str, str] = (
        "xpath",
        "//button[contains(text(), 'Войти')]",
    )
    BREAD_TAB: tuple[str, str] = ("xpath", "//div[contains(@class, 'tab')][1]")
    SAUCES_TAB: tuple[str, str] = (
        "xpath",
        "//div[contains(@class, 'tab')][2]",
    )
    TOPPINGS_TAB: tuple[str, str] = (
        "xpath",
        "//div[contains(@class, 'tab')][3]",
    )
    BREAD_TITLE: tuple[str, str] = ("xpath", "//h2[contains(text(), 'Булки')]")
    SAUCES_TITLE: tuple[str, str] = (
        "xpath",
        "//h2[contains(text(), 'Соусы')]",
    )
    TOPPINGS_TITLE: tuple[str, str] = (
        "xpath",
        "//h2[contains(text(), 'Начинки')]",
    )


class LoginPageLocators:
    """Локаторы LoginPage"""

    LOGIN_INPUT: tuple[str, str] = ("xpath", "//input[@type='text']")
    PASSWORD_INPUT: tuple[str, str] = ("xpath", "//input[@type='password']")
    LOGIN_BUTTON: tuple[str, str] = (
        "xpath",
        "//button[contains(@class, 'button')]",
    )


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


class ForgotPasswordPageLocators:
    """Локаторы страницы ForgotPasswordPage"""

    LOGIN_LINK: tuple[str, str] = ("xpath", "//a[@href='/login']")


class AccountProfilePageLocators:
    """Локаторы страницы AccountProfilePage"""

    EXIT_BUTTON: tuple[str, str] = (
        "xpath",
        "//button[contains(text(), 'Выход')]",
    )
