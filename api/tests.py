from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):

    def test_get_all_products(self):
        """
        Ensure we can retrive the objects in database
        """
        Product(name='My first product', description='Description of product 1', price=10.99).save()
        Product(name='My second product', description='Description of product 2', price=119.00).save()

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('My first product' in dict(response.data[0])['name'])
        self.assertTrue('Description of product 1' in dict(response.data[0])['description'])
        self.assertTrue('10.99' in dict(response.data[0])['price'])

        self.assertTrue('My second product' in dict(response.data[1])['name'])
        self.assertTrue('Description of product 2' in dict(response.data[1])['description'])
        self.assertTrue('119.00' in dict(response.data[1])['price'])

    def test_get_a_product(self):
        """
        Ensure we can retrive a specificy object in database using the id
        """
        Product(name='My first product', description='Description of product 1', price=10.99).save()

        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('My first product' in dict(response.data)['name'])
        self.assertTrue('Description of product 1' in dict(response.data)['description'])
        self.assertTrue('10.99' in dict(response.data)['price'])
