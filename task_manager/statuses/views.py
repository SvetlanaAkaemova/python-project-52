from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Status
from task_manager.users.views import UserCheckMixin
from task_manager.statuses.forms import StatusCreateForm


class IndexView(UserCheckMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'


class StatusCreateView(UserCheckMixin, SuccessMessageMixin, CreateView):
    form_class = StatusCreateForm
    success_message = _('Status was created successfully')
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/create.html'


class StatusUpdateView(UserCheckMixin, SuccessMessageMixin, UpdateView):

    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusCreateForm
    success_message = _('Status was updated successfully')
    success_url = reverse_lazy('statuses')


class StatusDeleteView(UserCheckMixin, SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'statuses/delete.html'
    success_message = _('Status was deleted successfully')
    success_url = reverse_lazy('statuses')
