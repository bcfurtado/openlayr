from django.core.urlresolvers import resolve
from django.test import TestCase
from store import home_page


def HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found, home_page)
