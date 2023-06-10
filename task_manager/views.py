from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')
    next_page = reverse_lazy('home')
    template_name = 'login.html'


class UserLogoutView(SuccessMessageMixin, LogoutView):
#    success_url = reverse_lazy('home')
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, _('You are logged out'))
        return response
