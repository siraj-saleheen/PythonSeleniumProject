#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class SearchResultPage(object):
        
    def __init__(self, driver):
        self.driver = driver
        self.result_page_title = "Google"
        self.search_field = "input[name='q']"

    def enter_search_term(self, search_term):
        """ enters a string value in the search field """
        elem = self.driver.find_element_by_css_selector(self.search_field)
        print(elem)
        elem.clear()
        elem.send_keys(search_term)
        elem.send_keys(Keys.RETURN)
    
    def wait_for_googel_search_page_element_loaded(self, css_locator, wait_time=10):
        """
        - Waits for and element on the page to load
        :param wait_time: maximum time to wait for page loading. Default=10s.
        :param css_locator: the css locator of the element.
        :return: bool
        """
        def wait_for_element(driver):
            elem = self.driver.find_element_by_css_selector(css_locator)
            return True if elem else False
        try:
            return WebDriverWait(self.driver, wait_time).until(wait_for_element)
        except TimeoutException:
            return False