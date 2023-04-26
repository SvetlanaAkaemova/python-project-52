from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Status
from task_manager.statuses.forms import StatusCreateForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/index.html', context={
            'statuses': statuses,
        })


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusCreateForm
    success_message = _('Status was created successfully')
    success_url = reverse_lazy('statuses')
    template_name = 'statuses/create.html'


class StatusUpdateView(SuccessMessageMixin, UpdateView):

    model = Status
    template_name = 'statuses/update.html'
    form_class = StatusCreateForm
    success_message = _('Status was updated successfully')
    success_url = reverse_lazy('statuses')


class StatusDeleteView(SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'statuses/delete.html'
    success_message = _('Status was deleted successfully')
    success_url = reverse_lazy('statuses')
