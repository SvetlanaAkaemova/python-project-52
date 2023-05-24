from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import User
from task_manager.users.forms import UserRegisterForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
            return redirect(reverse_lazy('login'))
        return super(MyMessageMixin, self).dispatch(request, *args, **kwargs)


class UserCheckMixin(MyMessageMixin, UserPassesTestMixin):
    message_no_permission = _('You do not have rights to change another user.')
    unsuccess_url = reverse_lazy('users')

    def test_func(self):
        user = self.get_object()
        return user.id == self.request.user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            user = self.get_object()
            if user.id != self.request.user.id:
                messages.warning(self.request, self.message_no_permission)
                return redirect(self.unsuccess_url)
        else:
            return redirect(reverse_lazy('users'))


class UserUpdateView(UserCheckMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'users/update.html'
    form_class = UserRegisterForm
    success_message = _('User was updated successfully')
    success_url = reverse_lazy('users')


class UserDeleteView(UserCheckMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_message = _('User was deleted successfully')
    success_url = reverse_lazy('users')
