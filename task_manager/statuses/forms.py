from django.forms import ModelForm
from .models import Status
from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import PlaceholderMixin


class StatusCreateForm(PlaceholderMixin, ModelForm):

    class Meta:
        model = Status
        labels = {'name': _('Name')}
        fields = ['name']
