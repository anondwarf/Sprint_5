# coding=utf-8
class Locators:

    REGISTRATION_NAME_INPUT: str = (
        '//label[contains(text(), "Имя")]/following-sibling::input'
    )
    REGISTRATION_EMAIL_INPUT: str = (
        '//label[contains(text(), "Email")]/following-sibling::input'
    )
    REGISTRATION_PASSWORD_INPUT: str = (
        '//label[contains(text(), "Пароль")]/following-sibling::input'
    )
    REGISTRATION_BUTTON: str = '//*[@id="root"]/div/main/div/form/button'
    REGISTRATION_ERROR_PASSWORD: str = '//p[contains(text(), "Некорректный пароль")]'
    MAIN_ENTER_ACCOUNT_BUTTON: str = '//button[contains(text(), "Войти")]'
    FORGOT_PASS_ENTER_LINK: str = '//*[@id="root"]/div/main/div/div/p/a'
    REGISTRATION_ENTER_LINK: str = '//*[@id="root"]/div/main/div/div/p/a'
    HEADER_ENTER_LINK: str = '//*[@id="root"]/div/header/nav/a'
    ACCOUNT_PROFILE_EXIT_BUTTON: str = '//button[contains(text(), "Выход")]'
    MAIN_TOPPING_TAB: str = '//span[contains(text(), "Начинки")]/parent::*'
    MAIN_TOPPING_HEADER: str = '//h2[contains(text(), "Начинки")]'
    MAIN_SAUCES_TAB: str = '//span[contains(text(), "Соусы")]/parent::*'
    MAIN_SAUCES_HEADER: str = '//h2[contains(text(), "Соусы")]'
    MAIN_BREAD_TAB: str = '//span[contains(text(), "Булки")]/parent::*'
    MAIN_BREAD_HEADER: str = '//h2[contains(text(), "Булки")]'
    LOGIN_EMAIL_INPUT: str = (
        '//label[contains(text(), "Email")]/following-sibling::input'
    )
    LOGIN_PASSWORD_INPUT: str = (
        '//label[contains(text(), "Пароль")]/following-sibling::input'
    )
    LOGIN_ENTER_BUTTON: str = '//*[@id="root"]/div/main/div/form/button'
