from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView

from task_manager.users.views import UserCheckMixin
from .filters import TasksFilters
from .models import Task
from task_manager.labels.models import Label
from task_manager.tasks.forms import TaskCreateForm


class IndexView(FilterView):

    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    filterset_class = TasksFilters


class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = TaskCreateForm
    success_message = _('Task was created successfully')
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_context_data(self, *args, **kwargs):
        labels = Label.objects.filter(task=self.get_object())
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        context['labels'] = labels
        return context


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
