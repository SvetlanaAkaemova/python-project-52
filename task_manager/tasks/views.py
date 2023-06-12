from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView

from .filters import TasksFilters
from .models import Task
from task_manager.labels.models import Label
from task_manager.tasks.forms import TaskCreateForm
from task_manager.users.views import MyMessageMixin


class IndexView(MyMessageMixin, FilterView):

    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    filterset_class = TasksFilters


class TaskCreateView(MyMessageMixin, SuccessMessageMixin, CreateView):
    form_class = TaskCreateForm
    success_message = _('Task was created successfully')
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(MyMessageMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, *args, **kwargs):
        labels = Label.objects.filter(task=self.get_object())
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        context['labels'] = labels
        return context


class TaskUpdateView(MyMessageMixin, SuccessMessageMixin, UpdateView):

    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskCreateForm
    success_message = _('Task was updated successfully')
    success_url = reverse_lazy('tasks')


class TaskDeleteView(MyMessageMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    model = Task
    message_no_permission = _('Only the author can delete a task')
    template_name = 'tasks/delete.html'
    success_message = _('Task was deleted successfully')
    success_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return task.creator == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            task = self.get_object()
            if task.creator != self.request.user:
                messages.warning(self.request, self.message_no_permission)
        return redirect(self.success_url)
