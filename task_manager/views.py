from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

# def home(request):
#    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')
    success_url = reverse_lazy('home')
    template_name = 'login.html'


class UserLogoutView(SuccessMessageMixin, LogoutView):
    success_message = _('You are logged out')
    success_url = reverse_lazy('home')
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, _('You are logged out'))
        return response

# def user_logout(request):
#    logout(request)
#    messages.info(request, _('You are logged out'))
#    return redirect('home')
