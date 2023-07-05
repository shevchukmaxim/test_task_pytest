from typing import Any, Callable, cast, Optional, Tuple

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from ..default import ELEMENT_TIMEOUT, REPEAT_ACTION_TIMEOUT
from ..driver import Driver
from ..utils.webdriver_wait_for import wait_for

Locator = Tuple[By, str]


class BaseElement:
    def __init__(self, locator_type: By, locator: str,
                 name: Optional[str] = None):
        self._driver: Driver = Driver()
        self._locator = locator_type, locator
        self._name = name or locator

    @property
    def name(self) -> str:
        return f"{type(self).__name__} '{self._name}'"

    @property
    def text(self) -> str:
        return cast(str, self._find_element().text)

    def get_element_attribute(self, attribute: str) -> str:
        return self._find_element().get_attribute(attribute)

    @property
    def value(self) -> str:
        return cast(str, self._find_element().get_attribute("value"))

    def is_present(self, timeout: float = ELEMENT_TIMEOUT) -> bool:
        try:
            self._wait_for_condition(EC.visibility_of_element_located, "isn't visible", timeout)
            return True
        except TimeoutException:
            return False

    def is_enabled(self) -> bool:
        return self._find_element().is_enabled()

    def is_absent(self, timeout: float) -> bool:
        try:
            self._wait_for_condition(EC.invisibility_of_element_located,
                                     "exists", timeout)
            return True
        except TimeoutException:
            return False

    def _find_element(self) -> WebElement:
        return self._wait_for_condition(EC.presence_of_element_located, "wasn't found")

    def _wait_for_condition(self, condition: Callable[[Locator], Any],
                            message: str, timeout: float = ELEMENT_TIMEOUT) -> WebElement:
        try:
            wait = self._driver.wait(timeout=timeout)
            element = wait.until(condition(self._locator))
        except TimeoutException:
            result_message = f"Element `{self.name}` with locator `{self._locator}` {message}"
            raise TimeoutException(result_message)
        return element

    @property
    def screenshot_as_base64(self) -> str:
        return cast(str, self._find_element().screenshot_as_base64)

    def mouse_to_element(self, timeout: int = REPEAT_ACTION_TIMEOUT) -> None:
        def func():
            try:
                ActionChains(self._driver).move_to_element(
                    self._find_element()).perform()
                return True
            except Exception as err:
                # logger.warn(err)
                return False
        wait_for(self._driver, func, timeout)

    def get_value_of_css_property(self, css_property: str) -> str:
        return self._find_element().value_of_css_property(css_property)

    @property
    def size(self):
        return self._find_element().size

    @property
    def location(self):
        return self._find_element().location

    def click(self, timeout: int = REPEAT_ACTION_TIMEOUT) -> None:
        def func():
            try:
                self._wait_to_be_clickable().click()
                return True
            except StaleElementReferenceException:
                # logger.warn(f"StaleElement error occurred while clicking")
                pass
            return False
        wait_for(self._driver, func, timeout)


    def _wait_to_be_clickable(self) -> WebElement:
        return self._wait_for_condition(EC.element_to_be_clickable, "isn't clickable")
