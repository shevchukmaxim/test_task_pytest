from typing import Any, Dict, Optional, Type

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from .default import ELEMENT_TIMEOUT, ELEMENT_POLL_FREQUENCY


class Singleton(type):
    _instances: Dict[Type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances.update(
                {cls: super().__call__(*args, **kwargs)}
            )
        return cls._instances[cls]


class Driver(metaclass=Singleton):

    def __init__(self) -> None:
        self._driver: Optional[WebDriver] = None

    def setup_driver(self, wd: WebDriver) -> None:
        self._driver = wd

    def wait(self, timeout: float = ELEMENT_TIMEOUT,
             poll_frequency: float = ELEMENT_POLL_FREQUENCY) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout, poll_frequency)

    @property
    def actions(self) -> ActionChains:
        return ActionChains(self._driver)

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._driver, attr)
