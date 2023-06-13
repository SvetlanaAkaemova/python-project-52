import pytest
from django.urls import reverse


@pytest.mark.parametrize('param', ['home', 'login'])
def test_render_views(client, param):
    temp_url = reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200
