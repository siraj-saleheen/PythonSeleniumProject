#!/usr/bin/env python3
# Author = Siraj Saleheen

import sys
sys.path.append('../')
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException, TimeoutException

@pytest.mark.usefixtures("initialize_chrome_driver")
class GoogleSearchPage:
    
    # path_to_chrome_driver = "/Users/ssaleheen/virtualenvs/a-python-selenium-sample-project/a-python-selenium-sample-project/lib/python3.6/site-packages/selenium/chromedriver"
    
    def __init__(self):
        # self.driver = webdriver.Chrome(self.path_to_chrome_driver)
        self.google_search_page_url = "https://google.com"
        self.title = "Google"
        self.search_field = "input[name='q']"
    
    def enter_search_term(self, search_term):
        elem = self.driver.find_element_by_css_selector(self.search_field)
        elem.clear()
        elem.send_keys(search_term)
        elem.send_keys(Keys.RETURN)

    def verify_page_title(self):
        return True if "Google Search" in self.driver.title else False

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