#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class BasePageHelper(object):

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def verify_page_title(self, title):
        """ verifies the page title """
        return True if title in self.driver.title else False