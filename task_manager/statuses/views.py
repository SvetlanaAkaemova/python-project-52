from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError

from .models import Status
from task_manager.statuses.forms import StatusCreateForm


class IndexView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusCreateForm
    success_message = _('Status was created successfully')
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/create.html'


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusCreateForm
    success_message = _('Status was updated successfully')
    success_url = reverse_lazy('statuses')


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'statuses/delete.html'
    message_no_permission = _('Can not delete status because it is in use')
    success_message = _('Status was deleted successfully')
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.warning(self.request, self.message_no_permission)
        finally:
            return redirect(success_url)
