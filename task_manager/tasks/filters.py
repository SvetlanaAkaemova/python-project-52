import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label
from .models import Task


class TasksFilters(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        field_name='self_tasks',
        method='get_self_tasks',
        widget=forms.CheckboxInput,
        label=_('Only your tasks')
    )
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def get_self_tasks(self, queryset, name, value):
        if value:
            queryset = queryset.filter(creator=getattr(self.request, 'user', None))
        return queryset
