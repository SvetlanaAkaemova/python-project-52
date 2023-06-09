from django.forms import ModelForm
from .models import Label
from task_manager.users.forms import PlaceholderMixin


class LabelCreateForm(PlaceholderMixin, ModelForm):

    class Meta:
        model = Label
        fields = ['name']
