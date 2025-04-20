from django.test import TestCase, Client
from django.urls import reverse
from cardekho_app.models import CarList
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.car_list = reverse('car_list')
        self.detail_url = reverse('car_detail', args=[1])
        self.car = CarList.objects.create(
            name='Toyota', description='Camry', active="True"
        )

    def test_car_list_view_GET(self):

        response = self.client.get(self.car_list)

        self.assertEqual(response.status_code, 200)
    
    def test_car_detail_view_GET(self):

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
    
    def test_car_list_view_POST(self):

        response = self.client.post(self.car_list, {
            'name': 'test_car',
            'description': 'New Car',
            'active': "True",
            'chassisnumber': '12345',
            'price': '200000',
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CarList.objects.count(), 2)
    
    def test_car_detail_view_DELETE(self):

        CarList.objects.create(
            name='test_car',
            description='New Car',
            active="True",
            chassisnumber='12345',
            price='200000',
        )
        response = self.client.delete(self.detail_url, {'id': 2})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(CarList.objects.count(), 1)