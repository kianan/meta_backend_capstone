# unit test for views

from django.test import TestCase
from restaurant.models import *
from restaurant.views import *

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class SingleMenuItemViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.menu_item = Menu.objects.create(title="Test Menu", price=10.99, inventory=5)
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

    def setUp(self):
        # Set up test client and authenticate the user
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_retrieve_menu_item(self):
        url = reverse('single_menu_item', args=[self.menu_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.menu_item.title)

    def test_update_menu_item(self):
        url = reverse('single_menu_item', args=[self.menu_item.id])
        data = {'title': 'Updated Menu', 'price': 15.99, 'inventory': 3}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.title, 'Updated Menu')

    def test_delete_menu_item(self):
        url = reverse('single_menu_item', args=[self.menu_item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Menu.objects.filter(id=self.menu_item.id).exists())