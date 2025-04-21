from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import Todo


class TodoAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='tester', password='#testpass123')
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test task',
            description='Test description',
            status='Pending'
        )

    def test_redirects_if_user_not_authenticated(self):
        """Should redirect unauthenticated user to login page."""
        response = self.client.get(reverse('todo_list'))
        self.assertRedirects(response, '/login/?next=/')

    def test_user_can_login_with_valid_credentials(self):
        """Should log in successfully with correct credentials."""
        response = self.client.post(reverse('login'), {'username': 'tester', 'password': '#testpass123'})
        self.assertRedirects(response, reverse('todo_list'))

    def test_logged_in_user_can_create_todo(self):
        """Should allow logged-in user to create a new todo."""
        self.client.login(username='tester', password='#testpass123')
        self.client.post(reverse('add_todo'), {'title': 'New task', 'description': 'New description'})
        self.assertEqual(Todo.objects.filter(user=self.user).count(), 2)

    def test_owner_can_update_todo_status(self):
        """Should allow the owner to update todo status."""
        self.client.login(username='tester', password='#testpass123')
        self.client.post(reverse('update_status', args=[self.todo.id]), {'status': 'Done'})
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.status, 'Done')

    def test_non_owner_cannot_update_todo_status(self):
        """Should not allow non-owner to update todo status."""
        User.objects.create_user(username='other', password='123456')
        self.client.login(username='other', password='123456')
        self.client.post(reverse('update_status', args=[self.todo.id]), {'status': 'Done'})
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.status, 'Pending')