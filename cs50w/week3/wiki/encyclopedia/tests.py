from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestRoutes(TestCase):

    def test_index_view_status_200(self):

        # create a url to page to be tested. use reverse() method with "app_name:view_name"
        url = reverse("encyclopedia:index")
        # visit url using client.get(url), this is a class so need to use self.client.get(url)
        response = self.client.get(url)


        # test for status code 200, and a word shown on html page
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Encyclopedia")




 
 
