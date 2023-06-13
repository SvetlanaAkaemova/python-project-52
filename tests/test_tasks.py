import pytest
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.users.models import User


@pytest.mark.django_db
def test_task_create(
        client,
        authenticated_user,
        executor_for_task,
        task_data,
        test_status,
        test_label):
    url = reverse('tasks_create')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, task_data, follow=True)
    assert response.status_code == 200
    assert Task.objects.filter(name=task_data['name']).exists()


@pytest.mark.parametrize('param', ['tasks', 'tasks_create'])
@pytest.mark.django_db
def test_task_no_authenticate(client, param):
    url = reverse(param)
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_task_update(client, authenticated_user, test_task, task_data):
    update_url = reverse('tasks_update', args=[test_task.pk])
    response = client.get(update_url)
    assert response.status_code == 200

    task_data['name'] = 'Task2'
    response = client.post(update_url, task_data, follow=True)
    assert response.status_code == 200
    assert Task.objects.filter(name='Task2').exists()


@pytest.mark.django_db
def test_task_delete(client, authenticated_user, test_task):
    delete_url = reverse('tasks_delete', args=[test_task.pk])
    response = client.get(delete_url)
    assert response.status_code == 200

    response = client.post(delete_url, follow=True)
    assert response.status_code == 200
    assert Task.objects.filter(pk=test_task.pk).count() == 0


@pytest.mark.django_db
def test_task_delete_another_user(client, test_task):
    another_user = User.objects.create_user('another_user')
    client.force_login(another_user)
    delete_url = reverse('tasks_delete', args=[1])
    response = client.post(delete_url, follow=True)
    assert response.status_code == 200
    assert Task.objects.filter(pk=1).exists()
