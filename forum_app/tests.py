from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse


class LikeTests(APITestCase):

    def test_get_like(self):
        url = 'http://127.0.0.1:8000/api/forum/likes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_like(self):
    #     url = reverse('like-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_likes(self):
    #     url = reverse('like-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
