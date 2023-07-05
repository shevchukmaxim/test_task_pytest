from typing import Optional

from selenium.webdriver.common.by import By

from .default import ELEMENT_TIMEOUT
from .driver import Driver
from .elements.label import Label


class BaseScreen:
    def __init__(self, locator_type: By, locator: str,
                 name: Optional[str] = None):
        self._driver = Driver()
        self._locator_type = locator_type
        self._locator = locator
        self._name = name or locator

    def is_opened(self, timeout: float = ELEMENT_TIMEOUT) -> bool:
        return Label(self._locator_type, self._locator, self._name).is_present(timeout)

    def is_closed(self, timeout: float = ELEMENT_TIMEOUT) -> bool:
        return Label(self._locator_type, self._locator, self._name).is_absent(timeout)
