from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError

from .models import Label
from task_manager.users.views import UserCheckMixin
from task_manager.labels.forms import LabelCreateForm


class IndexView(UserCheckMixin, ListView):
    model = Label
    template_name = 'labels/index.html'


class LabelCreateView(UserCheckMixin, SuccessMessageMixin, CreateView):
    form_class = LabelCreateForm
    success_message = _('Label was created successfully')
    success_url = reverse_lazy('labels')
    template_name = 'labels/create.html'


class LabelUpdateView(UserCheckMixin, SuccessMessageMixin, UpdateView):

    model = Label
    template_name = 'labels/update.html'
    form_class = LabelCreateForm
    success_message = _('Label was updated successfully')
    success_url = reverse_lazy('labels')


class LabelDeleteView(UserCheckMixin, SuccessMessageMixin, DeleteView):

    model = Label
    template_name = 'labels/delete.html'
    message_no_permission = _('Can not delete label because it is in use')
    success_message = _('Label was deleted successfully')
    success_url = reverse_lazy('labels')

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            messages.warning(self.request, self.message_no_permission)
        finally:
            return redirect(success_url)
