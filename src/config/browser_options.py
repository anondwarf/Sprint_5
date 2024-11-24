from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class BrowsersOptions:
    """Класс настроек запуска браузеров"""

    @staticmethod
    def chrome_options() -> ChromeOptions:
        """Настройки запуска Chrome"""
        opt = ChromeOptions()
        opt.add_argument("--headless:new")
        return opt

    @staticmethod
    def firefox_options() -> FirefoxOptions:
        """Настройки запуска Firefox"""
        opt = FirefoxOptions()
        opt.add_argument("--headless:new")
        return opt
