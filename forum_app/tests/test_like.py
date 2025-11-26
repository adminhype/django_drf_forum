from rest_framework.test import APITestCase
from rest_framework import status


from django.urls import reverse
from django.contrib.auth.models import User


from forum_app.models import Question, Like


class LikeTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='fan', password='testpass')
        self.other_user = User.objects.create_user(
            username='hater', password='otherpass')
        self.question_author = User.objects.create_user(
            username='author', password='authorpass')

        self.question = Question.objects.create(
            title='Great Question',
            content='pls like',
            author=self.question_author,
            category='frontend'
        )
        self.list_url = reverse('like-list')

    def test_like_success(self):
        """
        test that a user can like a question successfully.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'question': self.question.id
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)

        like = Like.objects.get()
        self.assertEqual(like.user, self.user)  # right user?
        self.assertEqual(like.question, self.question)  # right question?

    def test_duplicate_like_failure(self):
        """
        test that a user cannot like the same question more than once.
        """
        Like.objects.create(user=self.user, question=self.question)
        self.client.force_authenticate(user=self.user)
        data = {
            'question': self.question.id
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Like.objects.count(), 1)

    def test_delete_other_like_forbidden(self):
        """
        test that a user cannot delete another users like.
        """
        like = Like.objects.create(user=self.user, question=self.question)
        detail_url = reverse('like-detail', kwargs={'pk': like.id})
        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Like.objects.count(), 1)
