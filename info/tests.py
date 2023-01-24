from django.test import TestCase
from django.urls import reverse


class TestInfoView(TestCase):
    """
    Testing info views
    """
    def test_info_page(self):
        response = self.client.get(reverse('info'))
        self.assertEqual(response.status_code, 200)
