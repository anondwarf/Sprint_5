from abc import ABC

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(ABC):
    """Класс конструктор для всех классов `*Page`"""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=10, poll_frequency=1)
        self.page_url = ""

    def open(self) -> None:
        self.driver.get(self.page_url)

    def is_opened(self) -> None:
        self.wait.until(ec.url_to_be(self.page_url))

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def enter_text(self, locator: tuple[str, str], text: str) -> None:
        self.wait.until(ec.element_to_be_clickable(locator)).send_keys(text)

    def is_entered_text(
        self, type: str, locator: tuple[str, str], text: str, attr: str = ""
    ) -> None:
        match type:
            case "value":
                self.wait.until(
                    ec.text_to_be_present_in_element_value(locator, text)
                )
            case "attr":
                self.wait.until(
                    ec.text_to_be_present_in_element_attribute(
                        locator, attr, text
                    )
                )
            case _:
                self.wait.until(
                    ec.text_to_be_present_in_element(locator, text)
                )

    def is_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
