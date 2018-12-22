#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
from lib.ui.pages.GoogleSearchPage import GoogleSearchPage
from lib.util.FontHelper import FontHelper
from lib.ui.pages.BasePageHelper import BasePageHelper

# @pytest.mark.usefixtures("initialize_chrome_driver")
class Test_VerifyGoogleSearchPageTitle:

    def test_verify_google_search_page_title(self):
        ## initialize webdriver
        driver = self.driver
        # instantiate page objects
        font_helper = FontHelper()
        google_search_page = GoogleSearchPage(driver)
        base_class = BasePageHelper(driver)
        # define variables
        PASS_PRINT = font_helper.set_pass_color_block(font_helper.OKGREEN)
        expected_title = google_search_page.page_title
        
        # checkpoint for page title
        assert base_class.verify_page_title(
            expected_title
            ), f'"{expected_title}" is not the correct title'
        print(f'{PASS_PRINT}Title "{expected_title}" is correct')