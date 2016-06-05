from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):

    def test_get_all_products(self):
        """
        Ensure we can retrive the objects in database
        """
        Product(name='My first product').save()
        Product(name='My second product').save()

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('My first product' in dict(response.data[0])['name'])
        self.assertTrue('My second product' in dict(response.data[1])['name'])
