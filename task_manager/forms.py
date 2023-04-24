from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _


#class CustomForm(AuthenticationForm):
#    username = forms.CharField(widget=TextInput(attrs={'placeholder': _(u'Username')}))
#    password = forms.CharField(label=_(u'Password'), widget=PasswordInput(attrs={'placeholder': _(u'Password')}))
