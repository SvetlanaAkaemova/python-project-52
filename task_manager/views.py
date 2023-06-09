from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


def home(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')
    success_url = reverse_lazy('home')
    template_name = 'login.html'


def user_logout(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return redirect('home')
