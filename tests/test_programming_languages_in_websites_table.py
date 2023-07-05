import pytest

from pages.programming_languages_in_websites_page import ProgrammingLanguagesInWebsitesPage

min_popularity_params = [
    10 ** 7,
    1.5 * 10 ** 7,
    5 * 10 ** 7,
    10 ** 8,
    5 * 10 ** 8,
    10 ** 9,
    1.5 * 10 ** 9
]


@pytest.fixture(autouse=True, scope="session")
def page():
    page = ProgrammingLanguagesInWebsitesPage()
    page.open_page()
    assert page.is_page_opened() is True
    yield page


@pytest.mark.parametrize("min_popularity", min_popularity_params)
def test_popularity_value_is_more_than_expected(min_popularity, page):
    errors = []
    rows = page.get_programming_languages_in_websites_table().get_rows()
    for row in rows:
        popularity = row.get_popularity_as_int()
        if popularity < min_popularity:
            error_message = f"{row.websites} (Frontend:{row.frontend}|Backend:{row.backend}) has {popularity} " \
                            f"unique visitors per month. (Expected more than {min_popularity})"
            errors.append(error_message)

    if errors:
        pytest.fail("\n".join(errors), pytrace=False)
