import pytest
from django.urls import reverse
from task_manager.labels.models import Label


@pytest.mark.django_db
def test_label_create(client, label_data):
    url = reverse('labels_create')
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, label_data, follow=True)
    assert response.status_code == 200
    assert Label.objects.filter(name=label_data['name']).exists()


@pytest.mark.django_db
def test_label_update(client, test_label, label_data):
    update_url = reverse('labels_update', args=[test_label.pk])
    response = client.get(update_url)
    assert response.status_code == 200

    label_data['name'] = 'Label2'
    response = client.post(update_url, label_data, follow=True)
    assert response.status_code == 200
    assert Label.objects.filter(name='Label2').exists()


@pytest.mark.django_db
def test_label_delete(client, test_label):
    delete_url = reverse('labels_delete', args=[test_label.pk])
    response = client.get(delete_url)
    assert response.status_code == 200

    response = client.post(delete_url, follow=True)
    assert response.status_code == 200
    assert Label.objects.filter(pk=test_label.pk).count() == 0


# @pytest.mark.django_db
# def test_label_delete_in_use(client, task):
#    delete_url = reverse('labels_delete', args=[1])
#    response = client.post(delete_url, follow=True)
#    assert response.status_code == 200
#    assert Label.objects.filter(pk=1).exists()
