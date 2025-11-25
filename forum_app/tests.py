from rest_framework.test import APITestCase
from rest_framework import status


from django.urls import reverse
from django.contrib.auth.models import User


from forum_app.api.serializers import QuestionSerializer
from forum_app.models import Question


class LikeTests(APITestCase):

    def test_get_like(self):
        url = 'http://127.0.0.1:8000/api/forum/likes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class QuestionTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.question = Question.objects.create(
            title='Test Question', content='test content', author=self.user, category='frontend')

    def test_detail_question(self):
        url = reverse('question-detail', kwargs={'pk': self.question.id})
        response = self.client.get(url)
        expected_data = QuestionSerializer(self.question).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
