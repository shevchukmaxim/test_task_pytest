from typing import Optional, List

from selenium.webdriver.common.by import By

from ..elements.base_element import BaseElement
from ..elements.list_of_elements import ListOfElements
from framework.utils.string_methods import remove_extra_details_from_string


class Table(BaseElement):
    class TableHeader(BaseElement):
        pass

    class TableBody(ListOfElements):
        pass

    class Row(BaseElement):
        pass

    def __init__(self, locator_type: By = None, locator: str = None,
                 table_header: TableHeader = None, table_body: TableBody = None,
                 name: Optional[str] = None):
        super().__init__(locator_type, locator, name)
        self.table_header = table_header or self.TableHeader(self._locator[0], self._locator[1] + "//thead//tr",
                                                             "Table header")
        self.table_body = table_body or self.TableBody(self.Row, self._locator[0], self._locator[1] + "//tbody//tr",
                                                       "Table rows")

    @property
    def header(self):
        header = [item.replace("\n", " ") for item in self.table_header.get_element_attribute("innerText").split('\t')]
        return [remove_extra_details_from_string(item) for item in header]

    @property
    def rows(self):
        rows = [row.get_element_attribute("innerText").replace('\n', '\t').split('\t') for row in
                self.table_body.get_elements()]
        return [[item.strip() for item in row] for row in rows]

    def get_rows_as_objects(self) -> List[Row]:
        return self.table_body.get_elements()

    def as_dict(self):
        return [dict(zip(self.header, row)) for row in self.rows]
