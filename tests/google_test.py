import pytest
import time

from pages.google_search_page import GoogleSearchPage


class TestGoogleSearchPage:
    @pytest.fixture
    def google_search_page(self, driver):
        return GoogleSearchPage(driver)

    @pytest.mark.google
    def test_google_search_page(self, google_search_page):
        google_search_page.perform_search('reddit')

        assert 'results' in google_search_page.result_stats
        assert 'seconds' in google_search_page.result_stats