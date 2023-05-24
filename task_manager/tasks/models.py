from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_creator')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='task_executor')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='task_status')
    timestamp = models.DateTimeField(auto_now_add=True)
    labels = models.CharField(max_length=100, blank=True)
