from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewUserSeeAllProductsInHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_show_all_products_in_store(self):

        self.fail('not implemented')
