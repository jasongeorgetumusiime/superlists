from django.test import TestCase
from django.urls import resolve, reverse

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