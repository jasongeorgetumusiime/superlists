import unittest

from selenium import webdriver


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
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She enter "Buy peackock feathers" into a textbox (Edith's hobby is tying 
        # fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1. By peacock feathers" as an item on the to-do list

        # There is still a text box inviting her to add another item. She enters "Use
        # peacock feahers to make a fly" (Edith is very methodical)

        # Edith wonders whether the site remembers her list. Then she sees a that the
        # site has generated a URL for her -- there is some explanatory text to that 
        # effect

        # She visits that URL -- her to do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')