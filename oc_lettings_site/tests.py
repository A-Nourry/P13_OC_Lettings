import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
