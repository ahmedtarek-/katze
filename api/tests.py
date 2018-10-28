from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status


class CatsAPITest(APITestCase):
    # Test for 5 cats endpoint
    client = APIClient()

    def setUp(self):
        url = reverse('cats')

    def test_get_five_cats(self):
        """
        This test ensures that we get five cats whenever
        we submit request to the cats endpoint
        """
        url = reverse('cats')
        response = self.client.get(reverse(url))

        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_five_cats_with_tag(self):
        """
        This test ensures that we get five cats whenever
        we submit request to the cats endpoint
        """
        tag = "jump"
        url = reverse('cats', args=[tag])
        response = self.client.get(reverse(url))

        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
