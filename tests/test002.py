#!/usr/bin/env python3
# Author = Siraj Saleheen
import sys
sys.path.append('../')
import pytest
from selenium import webdriver
# from lib.Util.BaseClass import BaseClass
from lib.UI.pages.GoogleSearchPage import GoogleSearchPage

@pytest.mark.usefixtures("initialize_chrome_driver")
class Test002:
    google_search_page_url = "https://google.com"
    search_term = "gil"        
    google_search_page = GoogleSearchPage()
    
    def test002_one(self):
        # launch the Google search page
        self.driver.get(self.google_search_page_url)
        # declare titles
        actual_title = self.driver.title
        expected_title = self.google_search_page.title
        # verify title text
        assert expected_title in actual_title, f'The title "{actual_title}" didn\'t match'
        self.google_search_page.enter_search_term(self.search_term)
        assert self.google_search_page.verify_page_title(), "FAIL"
            
    # def test002_one(self):
    #     try:
    #         # launch the Google search page
    #         self.driver.get(self.google_search_page_url)
    #         # # waits for page element to load
    #         # assert self.google_search_page.wait_for_googel_search_page_element_loaded(
    #         #     self.google_search_page.search_field)
    #         # declare titles
    #         actual_title = self.driver.title
    #         expected_title = self.google_search_page.title
    #         # verify title text
    #         assert expected_title in actual_title
    #     except (AssertionError):
    #         print(f'The title "{actual_title}" didn\'t match')

    #     try:
    #         self.google_search_page.enter_search_term(self.search_term)
    #         assert self.google_search_page.verify_page_title()
    #     except Exception as e2:
    #         print("The second exception is: ", e2)

# # instantiate the class        
# _test = Test001()
# #call function
# _test.test001()
# # quit webdriver
# _test.driver.quit()