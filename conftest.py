# #!/usr/bin/env python3
# # Author = Siraj Saleheen

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def initialize_chrome_driver(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("../lib/drivers/chromedriver.exe")
    # driver.get("https://google.com")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()