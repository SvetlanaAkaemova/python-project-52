from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError

from .models import User
from task_manager.users.forms import UserRegisterForm


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'


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

    def test_func(self):
        user = self.get_object()
        return user.id == self.request.user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            user = self.get_object()
            if user.id != self.request.user.id:
                messages.warning(self.request, self.message_no_permission)
        return redirect(self.success_url)


class UserUpdateView(UserCheckMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'users/update.html'
    form_class = UserRegisterForm
    success_message = _('User was updated successfully')
    message_no_permission = _('You do not have rights to change another user.')
    success_url = reverse_lazy('users')


class UserDeleteView(UserCheckMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'delete.html'
    success_message = _('User was deleted successfully')
    success_url = reverse_lazy('users')
    message_no_permission = _('You do not have rights to change another user.')
    message_no_deletion = _('Unable to delete user because it is in use')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.warning(self.request, self.message_no_deletion)
        finally:
            return redirect(success_url)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context = {
            'title': _('Deleting user'),
            'name': user.get_full_name(),
            'delete_url': reverse('users_delete', args=[user.id]),
        }
        return context
