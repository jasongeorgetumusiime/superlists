from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_an_empty_list_item(self):
        # Edith goes to the homepage and tries to enter and empty list item.
        # She hit Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request and does not load the the list page
        self.wait_for(lambda: self.browser.find_elements(
            By.CSS_SELECTOR, "#id_text:invalid"
        ))
        
        # She starts typing some text for a the new item and the error disappears
        self.get_item_input_box().send_keys("Buy coffee")
        self.wait_for(lambda: self.browser.find_elements(
            By.CSS_SELECTOR, "#id_text:invalid"
        ))
        
        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy coffee")

        # Perversely, she decided to submit another blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.check_for_row_in_list_table("1: Buy coffee")
        self.wait_for(lambda: self.browser.find_elements(
            By.CSS_SELECTOR, "#id_text:invalid"
        ))

        # And she can correct it by filling in some text
        self.get_item_input_box().send_keys("Make a cappucino")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy coffee")
        self.check_for_row_in_list_table("2: Make a cappucino")

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the homepage and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy wellies")

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)
                
        # Shee a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You've already got this on your list"
        ))