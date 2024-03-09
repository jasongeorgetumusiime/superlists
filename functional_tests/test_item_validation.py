from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_an_empty_list_item(self):
        # Edith goes to the homepage and tries to enter and empty list item.
        # She hit Enter on the empty input box

        # The homepage refreshes and there is an error message showing that the
        # list item cannot be blank

        # She re-tries with some text for the item, which bow works

        # Perversely, she decided to submit another blank list item

        #She receives a similar warning on the list page

        # And she can correct it by filling in some text
        self.fail('write me!') 