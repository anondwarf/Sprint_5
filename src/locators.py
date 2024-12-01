# coding=utf-8
class Locators:

    REGISTRATION_NAME_INPUT: str = (
        '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    )
    REGISTRATION_EMAIL_INPUT: str = (
        '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    )
    REGISTRATION_PASSWORD_INPUT: str = (
        '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    )
    REGISTRATION_BUTTON: str = '//*[@id="root"]/div/main/div/form/button'
    REGISTRATION_ERROR_PASSWORD: str = (
        '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'
    )
    MAIN_ENTER_ACCOUNT_BUTTON: str = '//*[@id="root"]/div/main/section[2]/div/button'
    FORGOT_PASS_ENTER_LINK: str = '//*[@id="root"]/div/main/div/div/p/a'
    REGISTRATION_ENTER_LINK: str = '//*[@id="root"]/div/main/div/div/p/a'
    HEADER_ENTER_LINK: str = '//*[@id="root"]/div/header/nav/a'
    ACCOUNT_PROFILE_EXIT_BUTTON: str = (
        '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    )
    MAIN_TOPPING_TAB: str = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'
    MAIN_TOPPING_HEADER: str = '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]'
    MAIN_SAUCES_TAB: str = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'
    MAIN_SAUCES_HEADER: str = '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]'
    MAIN_BREAD_TAB: str = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'
    MAIN_BREAD_HEADER: str = '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]'
