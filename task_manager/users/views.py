from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import User
from task_manager.users.forms import UserRegisterForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_message = _('User was registered successfully')
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'


class MyMessageMixin(LoginRequiredMixin):
    permission_denied_message = _('You are not logged in. Please log in.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, self.permission_denied_message)
            return self.handle_no_permission()
        return super(MyMessageMixin, self).dispatch(request, *args, **kwargs)


class UserUpdateView(MyMessageMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'users/update.html'
    form_class = UserRegisterForm
    permission_denied_message = _('You are not logged in. Please log in.')
    success_message = _('User was updated successfully')
    success_url = reverse_lazy('users')


class UserDeleteView(MyMessageMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    permission_denied_message = _('You are not logged in. Please log in.')
    success_message = _('User was deleted successfully')
    success_url = reverse_lazy('users')
