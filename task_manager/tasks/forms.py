from django.forms import ModelForm
from .models import Task
from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import PlaceholderMixin


class TaskCreateForm(PlaceholderMixin, ModelForm):

    class Meta:
        model = Task
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'executor': _('Executor'),
            'labels': _('Labels'),
            'status': _('Status'),
        }
        fields = ['name', 'description', 'status', 'executor', 'labels']
