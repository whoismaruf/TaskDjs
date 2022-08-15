from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Task


class TaskModelTest(TestCase):
    '''
        🧪 Testing the Task model.
    '''
    def create_test_user(self, username='test', password='test'):
        return User.objects.create_user(username=username, password=password)
    
    def test_create_task(self):
        user = self.create_test_user()
        self.assertEqual(user.username, 'test')
        task = Task.objects.create(name='test', tasker=user)
        self.assertEqual(task.name, 'test')
        