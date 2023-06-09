import pytest
from django.urls import reverse
from task_manager.users.models import User


@pytest.mark.django_db
def test_user_signup(client, user_data):
    assert User.objects.count() == 0
    signup_url = reverse('users_create')
    response = client.post(signup_url, user_data, follow=True)
    assert response.status_code == 200
    assert User.objects.filter(username=user_data['username']).exists()


@pytest.mark.django_db
def test_user_update(client, authenticated_user, new_user_data):
    update_url = reverse('users_update', args=[authenticated_user.pk])
    response = client.get(update_url)
    assert response.status_code == 200

    post_response = client.post(update_url, new_user_data, follow=True)
    assert post_response.status_code == 200
    assert User.objects.filter(username=new_user_data['username']).exists()


@pytest.mark.django_db
def test_user_update_no_authenticate(client, test_user):
    update_url = reverse('users_update', args=[test_user.pk])
    response = client.get(update_url)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_update_another_user(client, authenticated_user):
    another_user = User.objects.create_user('another_user')
    update_url = reverse('users_update', args=[another_user.pk])
    response = client.get(update_url)
    assert response.status_code == 302
    assert response.url == reverse('users')


@pytest.mark.django_db
def test_user_delete(client, authenticated_user):
    delete_url = reverse('users_delete', args=[authenticated_user.pk])
    response = client.get(delete_url, follow=True)
    assert response.status_code == 200

    post_response = client.post(delete_url, follow=True)
    assert post_response.status_code == 200
    assert User.objects.filter(pk=authenticated_user.pk).count() == 0


@pytest.mark.django_db
def test_user_delete_no_authenticate(client, test_user):
    delete_url = reverse('users_delete', args=[test_user.pk])
    response = client.get(delete_url)
    assert response.status_code == 302
    assert response.url == reverse('login')


@pytest.mark.django_db
def test_delete_another_user(client, authenticated_user):
    another_user = User.objects.create_user('another_user')
    delete_url = reverse('users_delete', args=[another_user.pk])
    response = client.get(delete_url)
    assert response.status_code == 302
    assert response.url == reverse('users')
