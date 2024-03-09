import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip

MAX_WAIT = 5


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.gecko_service = webdriver.FirefoxService(
            executable_path="/usr/bin/geckodriver")
        self.browser = webdriver.Firefox(service=self.gecko_service)

    def tearDown(self) -> None:
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        self.wait_for_row_in_list_table(row_text)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = self.browser.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)