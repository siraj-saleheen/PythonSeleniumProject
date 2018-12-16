#!/usr/bin/env python3
# Author = Siraj Saleheen
import pytest
import sys
sys.path.append('../')
from lib.UI.pages.GoogleSearchPage import GoogleSearchPage

class Test001:
    def __init__(self):
        # instance variables
        ####################        
        self.google_search_page = GoogleSearchPage()
        self.driver = self.google_search_page.driver
        self.google_search_page_url = "https://google.com"
        self.search_term = "gil"

    def test001(self):
        try:
            # launch the Google search page
            self.driver.get(self.google_search_page_url)
            # waits for page element to load
            assert self.google_search_page.wait_for_page_element_loaded(
                self.google_search_page.search_field)
            # declare titles
            actual_title = self.driver.title
            expected_title = self.google_search_page.title
            # verify title text
            assert expected_title in actual_title
        except (AssertionError):
            print(f'The title "{actual_title}" didn\'t match')
        # try:
        #     self.google_search_page.enter_search_term(self.search_term)
        #     assert self.google_search_page.verify_page_title()
        # except Exception as e2:
        #     print("The second exception is: ", e2)

# instantiate the class        
_test = Test001()
#call function
_test.test001()
# quit webdriver
_test.driver.quit()