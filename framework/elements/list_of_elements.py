from typing import  Callable, Optional, Generic, List, TypeVar

from selenium.webdriver.common.by import By

from framework.driver import Driver

T = TypeVar("T")


class ListOfElements(Generic[T]):

    def __init__(self, element_type: Callable[[By, str, str], T],
                 locator_type: By, locator: str,
                 name: Optional[str] = None):
        assert locator_type == By.XPATH
        self._driver = Driver()
        self._element_type: Callable[[By, str, str], T] = element_type
        self._locator_type = locator_type
        self._locator = locator
        self._name = name or locator

    @property
    def size(self) -> int:
        return len(self._driver.find_elements(self._locator_type,
                                              self._locator))

    def get_elements(self) -> List[T]:
        list_of_elements = []
        for i in range(1, self.size + 1):
            locator = f"{self._locator}[{i}]"
            name = f"{self._name}[{i}]"
            list_of_elements.append(
                self._element_type(self._locator_type, locator, name)
            )
        return list_of_elements
