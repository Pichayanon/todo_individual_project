from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Todo(models.Model):
    """
    Represents a task in the application.

    Attributes:
        user (User) : The user who owns this task.
        title (str) : The title of the task.
        description (str) : Optional detailed description of the task.
        status (str) : The current status of the task (Pending, In Progress, Done).
        created_at (datetime) : The date and time when the task was created.
        due_at (datetime) : The due date and time for the task.
        photo (CloudinaryField) : An optional photo related to the task, stored in Cloudinary.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(blank=True, null=True)
    photo = CloudinaryField('photo', blank=True, null=True, folder='todo_photos')

    def __str__(self):
        """ Return a text of the tasks. """
        return self.title
