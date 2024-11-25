# Sprint 5

UI тестирование сайта [stellarburgers.nomoreparties.site](https://stellarburgers.nomoreparties.site)

## Содержание

- [Sprint 5](#sprint-5)
  - [Содержание](#содержание)
  - [Запуск проекта](#запуск-проекта)
  - [Структура проекта](#структура-проекта)
    - [Корень проекта](#корень-проекта)
    - [`src/base`](#srcbase)
    - [`src/config`](#srcconfig)
    - [`src/pages`](#srcpages)
    - [`src/utils`](#srcutils)
    - [`tests`](#tests)
  - [Реализованные тесты](#реализованные-тесты)
    - [`TestRegistration`](#testregistration)
      - [`test_name_input`](#test_name_input)
      - [`test_email_input`](#test_email_input)
      - [`test_password_input_good`](#test_password_input_good)
      - [`test_password_input_bad_notice`](#test_password_input_bad_notice)
      - [`test_password_input_bad_input`](#test_password_input_bad_input)
      - [`test_registration`](#test_registration)
    - [`TestRedirectNotAuth`](#testredirectnotauth)
      - [`test_main_page_login_account_button`](#test_main_page_login_account_button)
      - [`test_base_page_account_link`](#test_base_page_account_link)
      - [`test_registration_page_login_link`](#test_registration_page_login_link)
      - [`test_forgot_password_login_link`](#test_forgot_password_login_link)
    - [`TestRedirectAuth`](#testredirectauth)
      - [`test_main_page_login_link`](#test_main_page_login_link)
      - [`test_account_profile_page_constructor_link`](#test_account_profile_page_constructor_link)
      - [`test_account_profile_page_logo`](#test_account_profile_page_logo)
    - [`TestAccountExit`](#testaccountexit)
      - [`test_exit_account`](#test_exit_account)

## Запуск проекта

```bash
poetry run pytest -n auto tests
```

```bash
pytest -n auto tests
```

## Структура проекта

```bash
.
├── README.md
├── conftest.py
├── poetry.lock
├── pyproject.toml
├── src
│   ├── base
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   └── base_test.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── browser_options.py
│   │   ├── links.py
│   │   └── locators.py
│   ├── pages
│   │   ├── __init__.py
│   │   ├── *_page.py
│   └── utils
│       ├── __init__.py
│       └── generation_data.py
└── tests
    └── registration_page
        ├── __init__.py
        └── test_*.py
```
### Корень проекта

### `src/base`

Классы конструкторы для классов `Page` & `Test`

### `src/config`

Конфигурация тестов и браузеров

### `src/pages`

Классы страниц проекта

### `src/utils`

Дополнительные классы помогающие в тестировании, например генерация тестовых данных

### `tests`

Классы тестов

## Реализованные тесты

### `TestRegistration`

Тесты на странице регистрации

#### `test_name_input`

Проверка возможности ввести имя

#### `test_email_input`

Проверка ввести email

#### `test_password_input_good`

Проверка возможности ввести пароль (более 7 символов)

#### `test_password_input_bad_notice`

Проверка, что при вводе пароля, менее 7 символов, появляется текстовое уведомление об ошибке

#### `test_password_input_bad_input`

Проверка, что при вводе пароля, менее 7 символов, `div` имеет класс `error`

#### `test_registration`

Тест регистрации на сайте

### `TestRedirectNotAuth`

Тесты не авторизированного пользователя

#### `test_main_page_login_account_button`

Тест проверяющий переход с главной страницы на страницу авторизации по кнопке "Войти в аккаунт"

#### `test_base_page_account_link`

Проверка перехода по ссылке из шапки сайта "Личный кабинет"

#### `test_registration_page_login_link`

Проверка перехода по ссылке "Войти" на страницу регистрации

#### `test_forgot_password_login_link`

Проверка перехода по ссылке "Войти" на странице восстановления пароля

### `TestRedirectAuth`

Тесты авторизированного пользователя

#### `test_main_page_login_link`

Проверка перехода в личный кабинет по ссылке "Личный кабинет" в шапке сайта

#### `test_account_profile_page_constructor_link`

Проверка перехода по ссылке "Конструктор" со страницы профиля, на главную страницу

#### `test_account_profile_page_logo`

Проверка перехода по ссылке из лого в шапке сайта со страницы профиля аккаунта на главную страницу

### `TestAccountExit`

#### `test_exit_account`

Проверка выхода из аккаунта