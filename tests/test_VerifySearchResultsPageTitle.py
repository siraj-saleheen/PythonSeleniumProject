#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
from lib.ui.pages.GoogleSearchPage import GoogleSearchPage
from lib.util.FontHelper import FontHelper
from lib.ui.pages.BasePageHelper import BasePageHelper

@pytest.mark.usefixtures("initialize_chrome_driver")
class Test_VerifySearchResultsPageTitle:

    def test_verify_search_results_page_title(self):
        # initialize webdriver
        driver = self.driver
        # instantiate page objects
        font_helper = FontHelper()
        base_class = BasePageHelper(driver)
        google_search_page = GoogleSearchPage(driver)
        # define variables
        PASS_PRINT = font_helper.set_pass_color_block(font_helper.OKGREEN)
        google_search_result_page_title = google_search_page.search_result_page_title
        # enter sring value to search field
        google_search_page.enter_search_term(google_search_page.search_term)
        # checkpoint for page title
        assert base_class.verify_page_title(
            google_search_result_page_title
            ), f'"{google_search_result_page_title}" is not the correct title'
        print(f'{PASS_PRINT}Title "{google_search_result_page_title}" is correct')        

