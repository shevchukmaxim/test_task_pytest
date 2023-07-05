from framework.default import FAST_LOAD_ELEMENT_TIMEOUT
from screens.programming_languages_in_websites_screen import ProgrammingLanguagesInWebsitesScreen, \
    ProgrammingLanguagesInWebsitesTable
from WebDriverManager import WebDriverManager


class ProgrammingLanguagesInWebsitesPage:
    def __init__(self):
        self._programming_languages_in_websites_screen = ProgrammingLanguagesInWebsitesScreen()
        self._url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

    def open_page(self):
        WebDriverManager().load_web_page(self._url)

    def is_page_opened(self) -> bool:
        return self._programming_languages_in_websites_screen.is_opened(FAST_LOAD_ELEMENT_TIMEOUT)

    def get_programming_languages_in_websites_table(self) -> ProgrammingLanguagesInWebsitesTable:
        return self._programming_languages_in_websites_screen.programming_languages_in_websites_table
