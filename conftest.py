#!/usr/bin/env python3

__author__ = "Siraj Saleheen"

import sys
import pytest
from selenium import webdriver

@pytest.fixture(autouse=True, scope="class")
def initialize_chrome_driver(request):
    platform_darwin = "darwin"
    platform_windows = "win32"
    actual_platform = sys.platform
    print("\n--------------------------------")
    print("Platform:", actual_platform)
    print("--------------------------------")
    print("Initiliazing Chrome driver...")
    print("--------------------------------")
    if actual_platform in platform_darwin:
        driver = webdriver.Chrome("./lib/drivers/chromedriver")
    elif actual_platform in platform_windows:
        driver = webdriver.Chrome("./lib/drivers/chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()