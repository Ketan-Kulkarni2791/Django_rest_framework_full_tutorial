from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cardekho_app.views import car_list_view, car_detail_view


class TestUrls(SimpleTestCase):
    def test_car_list_url(self):
        url = reverse('car_list')
        self.assertEqual(resolve(url).func, car_list_view)

    def test_car_detail_url(self):
        url = reverse('car_detail', args=['1'])
        self.assertEqual(resolve(url).func, car_detail_view)