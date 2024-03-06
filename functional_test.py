import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        driver_service = webdriver.FirefoxService(
            executable_path="/usr/bin/geckodriver")
        self.browser = webdriver.Firefox(service=driver_service)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # Edit has heard about a cool new online to-do app and she goes to check out its
        # homepage
        self.browser.get("http://localhost:8000")

        # She notices the a page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholer'), 'Enter a to-do item')

        # She enters "Buy peackock feathers" into a textbox (Edith's hobby is tying 
        # fly-fishing lures)
        inputbox.send_keys("Buy peackock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item on the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element('id_list_table')
        rows = self.browser.find_elements('tr', By.TAG_NAME)
        self.assertTrue(
            any(row.text == "1. Buy peacock feathers" for row in rows)
        )

        # There is still a text box inviting her to add another item. She enters "Use
        # peacock feahers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')

        # Edith wonders whether the site remembers her list. Then she sees a that the
        # site has generated a URL for her -- there is some explanatory text to that 
        # effect

        # She visits that URL -- her to do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')