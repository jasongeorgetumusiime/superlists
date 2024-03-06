from django.test import TestCase
from django.urls import resolve, reverse

from .models import Item
from .views import home_page


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        response = self.client.post(
            reverse("home"), 
            data={"item_text": "A new to-do item"})
        self.assertIn("A new to-do item", response.content.decode("utf8"))
        self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Second list item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, "The first (ever) list item")
        self.assertEqual(saved_items[1].text, "Second list item")