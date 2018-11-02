from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status


class CatsAPITest(APITestCase):
    """
    This test ensures that we get five cats whenever
    we submit request with valid tag to our cats endpoint
    """

    def setUp(self):
        self.client = APIClient()
        self.valid_tag = 'funny'
        self.upper_case_valid_tag = 'FUNNY'
        self.invalid_tag = 'fu-nny'
        self.not_found_tag = 'asdf'

    def test_get_five_cats_for_valid_tag(self):
        url = reverse('cats-api', kwargs={'tag': self.valid_tag})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_get_five_cats_for_upper_case_valid_tag(self):
        url = reverse('cats-api', kwargs={'tag': self.upper_case_valid_tag})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_invalid_tag(self):
        url = reverse('cats-api', kwargs={'tag': self.invalid_tag})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found_tag(self):
        url = reverse('cats-api', kwargs={'tag': self.not_found_tag})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
