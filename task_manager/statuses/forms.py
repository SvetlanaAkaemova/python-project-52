from django.forms import ModelForm
from .models import Status
from task_manager.users.forms import PlaceholderMixin


class StatusCreateForm(PlaceholderMixin, ModelForm):

    class Meta:
        model = Status
        fields = ['name']
