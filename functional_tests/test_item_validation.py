from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_an_empty_list_item(self):
        # Edith goes to the homepage and tries to enter and empty list item.
        # She hit Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The homepage refreshes and there is an error message showing that the
        # list item cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CLASS_NAME, 'has-error').text,
            "You can't have an empty list item"
        ))

        # She re-tries with some text for the item, which bow works
        self.get_item_input_box().send_keys("Buy coffee")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy coffee")

        # Perversely, she decided to submit another blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        #She receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CLASS_NAME, 'has-error').text,
            "You can't have an empty list item"
        ))

        # And she can correct it by filling in some text
        self.get_item_input_box().send_keys("Make a cappucino")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table("1: Buy coffee")
        self.check_for_row_in_list_table("2: Make a cappucino")