from django.test import TestCase
import datetime
from django.urls import reverse
from . import views
# Create your tests here.

class NewyearViewTests(TestCase):

    def test_correct_newyear_date(self):
        """ when month and day are both equal to 1 (new year's day)
            a message stating "YES" is returned 
        """
        response = self.client.get(reverse("newyear:celebrate"), {"now": datetime.datetime(2025, 1, 1)})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "YES")

