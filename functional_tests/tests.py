import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 5


class NewVisitorTest(LiveServerTestCase):
    def setUp(self) -> None:
        self.gecko_service = webdriver.FirefoxService(
            executable_path="/usr/bin/geckodriver")
        self.browser = webdriver.Firefox(service=self.gecko_service)

    def tearDown(self) -> None:
        self.browser.quit()

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
                # time.sleep(0.5)
    
    def check_for_row_in_list_table(self, row_text):
        self.wait_for_row_in_list_table(row_text)

    def test_can_start_a_list_for_one_user(self) -> None:
        # Edit has heard about a cool new online to-do app and she goes to check out its
        # homepage
        self.browser.get(self.live_server_url)

        # She notices the a page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She enters "Buy peackock feathers" into a textbox (Edith's hobby is tying 
        # fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item on the to-do list
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # There is still a text box inviting her to add another item. She enters "Use
        # peacock feahers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # The page updates and now she shes both items on her list
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user Francis comes along to the site

        ## We use a new broswer session to make sure no information os Edith's 
        ## Is comming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox(service=self.gecko_service)

        # Francis visits the homepage, there is no sign of edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        
        # Francis starts a new list by endtering a new item. He is less 
        # interesting than Edith
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again there is not trace of edith's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied they both go to sleep