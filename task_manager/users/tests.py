from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate
from task_manager.users.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            username='TestUser',
            password='testpassword'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_user(self):
        user = authenticate(username='TestUser', password='testpassword')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_user(self):
        user = authenticate(username='WrongUser', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='TestUser', password='wrongpassword')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_update_user(self):
        self.user.username = 'NewName'
        self.user.save()
        self.assertEqual(self.user.username, 'NewName')

    def test_delete_user(self):
        user = authenticate(username='TestUser', password='testpassword')
        user.delete()
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(pk=1)
