from selenium.webdriver.common.by import By

from .base_page import BasePage


class GoogleSearchPage(BasePage):
    _logo = {'by': By.ID, 'value': 'hplogo'}
    _result_stats = {'by': By.ID, 'value': 'resultStats'}
    _search_input = {'by': By.NAME, 'value': 'q'}

    def __init__(self, driver):
        super().__init__(driver)

        self._visit('/')

        assert self._is_displayed(self._logo)
        assert self._is_displayed(self._search_input)

    @property
    def result_stats(self):
        return self._find(self._result_stats).text

    def perform_search(self, search_query):
        self._type(self._search_input, search_query, clear_input=True, terminate_with_return_key=True)
