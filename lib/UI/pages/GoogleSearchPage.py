#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class GoogleSearchPage(object):
        
    def __init__(self, driver):
        self.driver = driver
        self.search_term = "Grape Ape"        
        self.page_title = "Google"
        self.search_result_page_title = f'{self.search_term} - Google Search'
        self.search_field = "input[name='q']"

    def enter_search_term(self, search_term):
        """ Enters a string value in the search field 
        :param search_term: the test string to be searched
        :returns: string         
        """
        _search_field = self.driver.find_element_by_css_selector(self.search_field)
        _search_field.clear()
        _search_field.send_keys(search_term)
        _search_field.send_keys(Keys.RETURN)
    
    # def get_page_title(self):
    #     """ Gets the page title.
    #     :param: none
    #     :returns: string 
    #     """
    #     return self.driver.title

    # def verify_page_title(self, title):
    #     """ Verifies the page title.
    #     :param title: title string to be verified
    #     :returns: True if successful, False otherwise.         
    #     """
    #     return True if title in self.get_page_title() else False

    def wait_for_element_loaded(self, css_locator, wait_time=10):
        """ Waits for an element on the page to load.
        :param wait_time: maximum time to wait for element loading. Default=10s.
        :param css_locator: the css locator of the element.
        :returns: True if successful, exceptions if any, False otherwise.         
        """
        def wait_for_element(driver):
            elem = self.driver.find_element_by_css_selector(css_locator)
            return True if elem else False
        try:
            return WebDriverWait(self.driver, wait_time).until(wait_for_element)
        except TimeoutException:
            return False