from typing import List

from selenium.webdriver.common.by import By

from framework.elements.table import Table
from framework.base_screen import BaseScreen
from dataclasses import dataclass

from framework.utils.string_methods import remove_extra_details_from_string, convert_string_with_punctuation_into_int


class ProgrammingLanguagesInWebsitesTable(Table):

    @dataclass
    class TableRow:
        websites: str
        popularity: str
        frontend: str
        backend: str
        database: str
        notes: str

        def get_popularity_as_int(self) -> int:
            popularity = remove_extra_details_from_string(self.popularity)
            popularity = convert_string_with_punctuation_into_int(popularity)
            return popularity

    def get_rows(self) -> List[TableRow]:
        table = self.as_dict()
        table_rows = []
        for item in table:
            websites = item.get('Websites')
            popularity = item.get('Popularity')
            frontend = item.get('Front-end')
            backend = item.get('Back-end')
            database = item.get('Database')
            notes = item.get('Notes')

            table_rows.append(self.TableRow(websites, popularity, frontend, backend, database, notes))

        return table_rows


class ProgrammingLanguagesInWebsitesScreen(BaseScreen):
    def __init__(self):
        super().__init__(By.XPATH, "//span[contains(@class, 'mw-page-title-main') and "
                                   "contains(text(), 'Programming languages used in most popular websites')]"
                         )

    @property
    def programming_languages_in_websites_table(self) -> ProgrammingLanguagesInWebsitesTable:
        return ProgrammingLanguagesInWebsitesTable(
            By.XPATH,
            "//caption[contains(text(), 'Programming languages used in most popular websites')]/.."
        )


