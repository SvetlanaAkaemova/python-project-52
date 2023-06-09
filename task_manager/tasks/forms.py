from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import PlaceholderMixin
from .models import Task


class TaskCreateForm(PlaceholderMixin, ModelForm):

    class Meta:
        model = Task
        labels = {
            'labels': _('Labels')
        }
        fields = ['name', 'description', 'status', 'executor', 'labels']
