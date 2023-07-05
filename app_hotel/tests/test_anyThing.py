from django.test import SimpleTestCase
from profile_api import views

class View(SimpleTestCase):
    def test_make_test(self):
        self.assertEqual(1,1)
        