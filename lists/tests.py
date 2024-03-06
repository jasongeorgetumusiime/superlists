from django.test import TestCase
from django.urls import resolve, reverse

from .models import Item
from .views import home_page


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        response = self.client.post('/', data={"item_text": "A new to-do item"})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertIn(new_item.text, "A new to-do item")
        
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={"item_text": "A new to-do item"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey1")
        Item.objects.create(text="itemey2")

        response = self.client.get(reverse("home"))
        self.assertContains(response, "itemey1")
        self.assertContains(response, "itemey2")


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