from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class HomePageShowTheProducts(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_shows_products(self):
        self.browser.get(self.live_server_url)

        self.assertIn('openlayr', self.browser.title)

        products = self.browser.find_element_by_id('products')
        self.assertIn(products, 'Macbook Pro 13 - 2013')
