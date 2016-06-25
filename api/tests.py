from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category

class ProductTests(APITestCase):

    def setUp(self):
        first_category = Category(name='first category', description='first category description')
        first_category.save()
        first_product = Product(name='My first product',
                description='Description of product 1',
                price=10.99,
                category=first_category)
        first_product.save()

        second_category = Category(name='second category', description='second category description')
        second_category.save()
        second_product = Product(name='My second product',
                description='Description of product 2',
                price=119.00,
                category=second_category)
        second_product.save()

        third_product = Product(name='My third product',
                description='Description of product 3',
                price=55.99,
                category=first_category)
        third_product.save()


    def test_get_all_products(self):
        """
        Ensure we can retrive the objects in database
        """
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('My first product' in dict(response.data[0])['name'])
        self.assertTrue('Description of product 1' in dict(response.data[0])['description'])
        self.assertTrue('10.99' in dict(response.data[0])['price'])
        self.assertTrue('first category' in dict(response.data[0])['category'])

        self.assertTrue('My second product' in dict(response.data[1])['name'])
        self.assertTrue('Description of product 2' in dict(response.data[1])['description'])
        self.assertTrue('119.00' in dict(response.data[1])['price'])
        self.assertTrue('second category' in dict(response.data[1])['category'])

    def test_get_a_product(self):
        """
        Ensure we can retrive a specificy object in database using the id
        """
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('My first product' in dict(response.data)['name'])
        self.assertTrue('Description of product 1' in dict(response.data)['description'])
        self.assertTrue('10.99' in dict(response.data)['price'])
        self.assertTrue('first category' in dict(response.data)['category'])

    def test_get_a_product_filter_by_category(self):
        """
        Ensure we can retrive only product from a specific category
        """
        category_id = 1
        response = self.client.get('/api/products/?category_id=' + str(category_id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.data))
        self.assertTrue('My first product' in dict(response.data[0])['name'])
        self.assertTrue('My third product' in dict(response.data[1])['name'])


class CategoryTest(APITestCase):

    def setUp(self):
        Category(name='first category', description='first category description').save()
        Category(name='second category', description='second category description').save()
        Category(name='third category', description='third category description').save()

    def test_get_all_the_categories(self):
        """
        Ensure we can retrive all the categories
        """
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual('first category', dict(response.data[0])['name'])
        self.assertEqual('first category description', dict(response.data[0])['description'])
        self.assertEqual('second category', dict(response.data[1])['name'])
        self.assertEqual('second category description', dict(response.data[1])['description'])
        self.assertEqual('third category', dict(response.data[2])['name'])
        self.assertEqual('third category description', dict(response.data[2])['description'])

    def test_get_a_specificy_category(self):
        """Ensure we can retrive a specificy category"""
        response = self.client.get('/api/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(1, dict(response.data)['id'])
        self.assertEqual('first category', dict(response.data)['name'])
        self.assertEqual('first category description', dict(response.data)['description'])

class OrderTest(APITestCase):

    def setUp(self):
        first_category = Category(name='first category', description='first category description')
        first_category.save()
        first_product = Product(name='My first product',
                description='Description of product 1',
                price=10.99,
                category=first_category)
        first_product.save()
        second_product = Product(name='My second product',
                description='Description of product 2',
                price=119.00,
                category=first_category)
        second_product.save()


    def test_create_a_new_order(self):
        response = self.client.post('/api/orders/', {
            'name': 'Jonh Doe',
            'email': 'john@doe.com',
            'address': 'Wall Street',
            'products': [1,2],
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual('Jonh Doe', dict(response.data)['name'])
        self.assertEqual('john@doe.com', dict(response.data)['email'])
        self.assertEqual('Wall Street', dict(response.data)['address'])
        self.assertEqual('Pending', dict(response.data)['status'])
        self.assertIsNotNone(dict(response.data)['created_at'])
        self.assertEqual([1,2], dict(response.data)['products'])
