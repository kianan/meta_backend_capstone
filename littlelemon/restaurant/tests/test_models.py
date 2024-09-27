from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Test Menu", price=10.99, inventory=10)
        itemstr = str(item)
        self.assertEqual(itemstr, "Test Menu : 10.99")