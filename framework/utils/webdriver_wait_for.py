from typing import Callable, TypeVar

from framework.driver import Driver
from framework.default import REPEAT_ACTION_TIMEOUT

T = TypeVar('T')


class ExpressionWrapper:
    """
    Wrapper for until expression in Selenium WebDriver
    """
    def __init__(self, expression):
        self.expression = expression

    def __call__(self, driver):
        return self.expression()


def wait_for(driver: Driver,
             expression: Callable[..., T],
             timeout: int=REPEAT_ACTION_TIMEOUT,
             message: str = ''
             ) -> T:
    """
    Wait for expression to resolve an element
    :param driver: selenium web driver
    :param expression: callable expression
    :param timeout: timeout for expression
    :param message: message in case of TimeoutException
    :return: web driver element
    """
    wait = driver.wait(timeout)
    return wait.until(ExpressionWrapper(expression), '{} operation failed after {} seconds'.format(message, timeout))
