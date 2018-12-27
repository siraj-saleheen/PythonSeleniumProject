#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException, TimeoutException

class BaseClass:

    @classmethod
    def setUpClass(cls):
        """ Reimplement this method in your test class to add test-specific setup before the first test method starts
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Reimplement this method in your test class to add test-specific cleanup after the last test method finishes
        """
        pass
        