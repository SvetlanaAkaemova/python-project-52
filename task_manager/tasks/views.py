from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Task
from task_manager.tasks.forms import TaskCreateForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.views import UserCheckMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', context={
            'tasks': tasks,
        })


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCreateForm
    success_message = _('Task was created successfully')
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):

    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskCreateForm
    success_message = _('Task was updated successfully')
    success_url = reverse_lazy('tasks')


class TaskDeleteView(UserCheckMixin, SuccessMessageMixin, DeleteView):

    model = Task
    message_no_permission = _('Only the author can delete a task')
    unsuccess_url = reverse_lazy('tasks')
    template_name = 'tasks/delete.html'
    success_message = _('Task was deleted successfully')
    success_url = reverse_lazy('tasks')
