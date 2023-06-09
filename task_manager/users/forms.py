from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': _(field.label)})


class UserRegisterForm(PlaceholderMixin, UserCreationForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'placeholder': _(u'Password')}), help_text=_('Your password must contain at least 3 characters.'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
