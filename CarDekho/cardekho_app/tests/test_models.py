from django.test import TestCase
from cardekho_app.models import CarList


class CarListTestCase(TestCase):
    def setUp(self):
        self.car1 = CarList.objects.create(
            name='Toyota',
            description='Corolla',
            active='True',
            chassisnumber='454564fnffnf',
        )
        self.car2 = CarList.objects.create(
            name='Honda',
            description='Civic',
            active='False',
            chassisnumber='987654321'
        )
    
    def test_car_list_creation(self):
        self.assertEqual(self.car1.name, 'Toyota')