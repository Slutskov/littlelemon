from django.test import TestCase
from restaurant import views, models, serializers
from rest_framework.test import APIClient
import pdb

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = models.Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = models.Menu.objects.create(title="Chocolate", price=10, inventory=10)

    def test_getall(self):
        queryset = models.Menu.objects.all()
        serializer = serializers.MenuSerializer(queryset, many=True)
        expected = [{'id': 2, 'title': 'IceCream', 'price': '80.00', 'inventory': 100}, {'id': 3, 'title': 'Chocolate', 'price': '10.00', 'inventory': 10}]
        output = [dict(item) for item in serializer.data]
        self.assertEqual(output, expected)


