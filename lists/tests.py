from django.test import TestCase
from django.urls import resolve, reverse

from .models import Item, List


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'home.html')

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = "Second list item"
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, "The first (ever) list item")
        self.assertEqual(saved_items[0].list, list_)
        self.assertEqual(saved_items[1].text, "Second list item")
        self.assertEqual(saved_items[1].list, list_)


class ListViewTest(TestCase):
    
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list/')
        self.assertTemplateUsed(response,'list.html')

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text="itemey 1", list=list_)
        Item.objects.create(text="itemey 2", list=list_)

        response = self.client.get('/lists/the-only-list/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

class NewListTest(TestCase):

    def test_can_save_POST_request(self):
        response = self.client.post('/lists/new', 
                                    data={"item_text": "A new to-do item"})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertIn(new_item.text, "A new to-do item")
        
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', 
                                    data={"item_text": "A new to-do item"})
        self.assertRedirects(response, '/lists/the-only-list/')