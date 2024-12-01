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
