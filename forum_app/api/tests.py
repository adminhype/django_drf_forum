# from rest_framework import APITestCase
# from rest_framework import status

# from django.urls import reverse
# from django.contrib.auth.models import User

# from forum_app.api.serializers import QuestionSerializer
# from forum_app.models import Question


# class QuestionViewSetTests(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser', password='testpassword')
#         self.admin = User.objects.create_superuser(
#             username='adminuser', password='adminpassword')
#         self.question = Question.objects.create(
#             title='test Question', content='test content', author=self.user, catergory='frontend')

#     def test_create_question(self):
#         url = reverse('question-list')
#         data = {
#             'title': 'New Question',
#             'content': 'New content',
#             'author': self.user.id,
#             'catergory': 'frontend'
#         }
#         # one way to authenticate
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Question.objects.count(), 2)

#     def test_get_question(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, QuestionSerializer(self.question).data)

#     def test_update_question_by_owner(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})
#         data = {
#             'title': 'Updated Question',
#             'content': 'Updated content',
#             'catergory': 'backend'
#         }

#         self.client.force_authenticate(user=self.user)
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.question.refresh_from_db()
#         self.assertEqual(self.question.title, 'Updated Question')

#     def test_update_question_by_admin(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})
#         data = {
#             'title': 'Admin Updated Question',
#             'content': 'Admin Updated content',
#             'catergory': 'backend'
#         }

#         self.client.force_authenticate(user=self.admin)
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.question.refresh_from_db()
#         self.assertEqual(self.question.title, 'Admin Updated Question')

#     def test_delete_question_by_admin(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})

#         self.client.force_authenticate(user=self.admin)
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Question.objects.count(), 0)

#     def test_unauthorized_update_question(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})
#         data = {
#             'title': 'Unauthorized Update',
#             'content': 'Should not be updated',
#             'catergory': 'backend'
#         }

#         self.client.force_authenticate(user=User.objects.create_user(
#             username='otheruser', password='otherpassword'))
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_unauthorized_delete_question(self):
#         url = reverse('question-detail', kwargs={'pk': self.question.id})

#         self.client.force_authenticate(user=User.objects.create_user(
#             username='otheruser2', password='otherpassword2'))
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(Question.objects.count(), 1)
