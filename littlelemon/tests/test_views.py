
from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(title="Pizza", price=150, inventory=50)

    def test_get_all(self):
       
        response = self.client.get('/restaurant/menu/')  

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        expected_data = [
            {
                "id": self.menu_item1.id,
                "title": "IceCream",
                "price": "80.00",  # Format selon votre sérialiseur
                "inventory": 100,
            },
            {
                "id": self.menu_item2.id,
                "title": "Pizza",
                "price": "150.00",
                "inventory": 50,
            },
        ]

        self.assertEqual(response.data, expected_data)
