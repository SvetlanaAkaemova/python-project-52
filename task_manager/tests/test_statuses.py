import pytest
from django.urls import reverse
from task_manager.statuses.models import Status


@pytest.mark.django_db
def test_status_create(client, authenticated_user, status_data):
    url = reverse('statuses_create')
    response = client.get(url)
    assert response.status_code == 200

    post_response = client.post(url, status_data, follow=True)
    assert post_response.status_code == 200
    assert Status.objects.filter(name=status_data['name']).exists()


@pytest.mark.django_db
def test_status_update(client, test_status, status_data):
    update_url = reverse('statuses_update', args=[test_status.pk])
    response = client.get(update_url)
    assert response.status_code == 200

    status_data['name'] = 'Status2'
    post_response = client.post(update_url, status_data, follow=True)
    assert post_response.status_code == 200
    assert Status.objects.filter(name='Status2').exists()


@pytest.mark.django_db
def test_status_delete(client, test_status):
    delete_url = reverse('statuses_delete', args=[test_status.pk])
    response = client.get(delete_url)
    assert response.status_code == 200

    post_response = client.post(delete_url, follow=True)
    assert post_response.status_code == 200
    assert Status.objects.filter(pk=test_status.pk).count() == 0
