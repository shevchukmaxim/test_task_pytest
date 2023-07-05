import pytest

from WebDriverManager import WebDriverManager


@pytest.fixture(autouse=True, scope="session")
def driver():
    wd = WebDriverManager()
    wd.start_session_if_not_created()

    yield

    wd.close_session_if_active()
