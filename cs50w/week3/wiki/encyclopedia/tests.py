from django.test import TestCase
from django.urls import reverse
from . import views
from unittest.mock import patch



# Create your tests here.

class EncyclopediaViewTests(TestCase):
        
    # test views

    # test index view
    def test_index_status_200(self):
        """ tests index view return 200 code when correctly called """

        url = reverse("encyclopedia:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # test correct title
        self.assertContains(response, "Encyclopedia")
    
        

    # test get_title view


    # Mock the storage to control the markdown
    @patch("encyclopedia.views.util.get_entry", return_value="# Liverpool\nYou'll Never Walk Alone")
    def test_entry_status_200(self, _):
        url = reverse("encyclopedia:get_title", kwargs={"title": "liverpool"})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "You&#x27;ll Never Walk Alone")       # note: Django templates automatically escape characters like ' into &#x27;
    
    



 

  

