from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_creator', verbose_name=_('Author'))
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='task_executor', verbose_name=_('Executor'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='task_status', verbose_name=_('Status'))
    timestamp = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label, through='TasksAndLabels', blank=True, verbose_name=_('Label'))

    def __str__(self):
        return self.name


class TasksAndLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
