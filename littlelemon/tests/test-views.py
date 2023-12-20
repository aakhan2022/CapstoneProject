from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        return Menu.objects.create(title='MangoShake', price=15, inventory=50)
    
    def test_getall(self):
        url = reverse('all-menu-items')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)